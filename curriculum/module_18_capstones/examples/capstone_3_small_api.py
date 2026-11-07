"""Capstone 3: a small REST API - clean service layer, thin FastAPI shell.

Needs the optional web extra: ``pip install -e ".[web]"``.
"""

# requires: fastapi, httpx

from dataclasses import dataclass, field

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field


# ---- service layer: plain Python, no web imports needed to test it ----------
class NotFoundError(Exception):
    """Raised when a book id does not exist."""


@dataclass
class BookService:
    _books: dict[int, dict[str, object]] = field(default_factory=dict)

    def add(self, title: str, pages: int) -> dict[str, object]:
        book = {"id": len(self._books) + 1, "title": title, "pages": pages}
        self._books[int(str(book["id"]))] = book
        return book

    def get(self, book_id: int) -> dict[str, object]:
        try:
            return self._books[book_id]
        except KeyError:
            raise NotFoundError(book_id) from None

    def search(self, text: str) -> list[dict[str, object]]:
        return [
            b for b in self._books.values() if text.lower() in str(b["title"]).lower()
        ]


# ---- web layer: translate HTTP <-> service calls ----------------------------
class BookIn(BaseModel):
    title: str = Field(min_length=1)
    pages: int = Field(gt=0)


service = BookService()
app = FastAPI(title="Books")


@app.post("/books", status_code=201)
def create_book(book: BookIn) -> dict[str, object]:
    return service.add(book.title, book.pages)


@app.get("/books/{book_id}")
def read_book(book_id: int) -> dict[str, object]:
    try:
        return service.get(book_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="book not found") from None


@app.get("/books")
def list_books(q: str = "") -> list[dict[str, object]]:
    return service.search(q)


if __name__ == "__main__":
    client = TestClient(app)
    print(client.post("/books", json={"title": "Fluent Python", "pages": 1012}).json())
    print(client.get("/books/1").json(), client.get("/books/5").status_code)
    print(client.get("/books", params={"q": "python"}).json())
    print(client.post("/books", json={"title": "", "pages": 0}).status_code)
