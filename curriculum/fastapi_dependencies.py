"""FastAPI dependency injection: share a repository between routes."""

# requires: fastapi, httpx

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel


class Note(BaseModel):
    text: str


class NoteRepo:
    """Plain Python storage - no web code, easy to test on its own."""

    def __init__(self) -> None:
        self._notes: dict[int, Note] = {}

    def add(self, note: Note) -> int:
        new_id = len(self._notes) + 1
        self._notes[new_id] = note
        return new_id

    def get(self, note_id: int) -> Note | None:
        return self._notes.get(note_id)


repo = NoteRepo()


def get_repo() -> NoteRepo:
    return repo


router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", status_code=201)
def create(note: Note, notes: NoteRepo = Depends(get_repo)) -> dict[str, int]:
    return {"id": notes.add(note)}


@router.get("/{note_id}", response_model=Note)
def read(note_id: int, notes: NoteRepo = Depends(get_repo)) -> Note:
    found = notes.get(note_id)
    if found is None:
        raise HTTPException(status_code=404, detail="note not found")
    return found


app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    client = TestClient(app)
    print(client.post("/notes", json={"text": "hello"}).json())
    print(client.get("/notes/1").json(), client.get("/notes/7").status_code)
    # Tests can swap the dependency for a fake:
    app.dependency_overrides[get_repo] = NoteRepo
    print(client.get("/notes/1").status_code)
