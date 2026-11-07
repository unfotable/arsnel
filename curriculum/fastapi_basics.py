"""FastAPI basics: path/query parameters, request bodies and errors.

Needs the optional web extra: ``pip install -e ".[web]"``.
"""

# requires: fastapi, httpx

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(title="ARSNEL demo")


class Item(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


ITEMS: dict[int, Item] = {}


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "hello"}


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int) -> Item:
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="item not found")
    return ITEMS[item_id]


@app.post("/items", status_code=201, response_model=Item)
def create_item(item: Item) -> Item:
    ITEMS[len(ITEMS) + 1] = item
    return item


@app.get("/search")
def search(q: str = "", limit: int = 10) -> dict[str, object]:
    hits = [i.name for i in ITEMS.values() if q.lower() in i.name.lower()]
    return {"q": q, "results": hits[:limit]}


if __name__ == "__main__":
    client = TestClient(app)  # calls the app in-process, no server needed
    print(client.get("/").json())
    print(client.post("/items", json={"name": "pen", "price": 1.5}).status_code)
    print(client.get("/items/1").json())
    print(client.get("/items/99").status_code, client.get("/items/99").json())
    print(
        client.post("/items", json={"name": "", "price": -1}).status_code
    )  # validation
    print(client.get("/search", params={"q": "pe"}).json())
