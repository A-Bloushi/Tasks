from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

items: dict[int, Item] = {}
next_id = 1


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/",response_model=Item)
def create_item(item: Item):
    global next_id
    items[next_id] = item
    created = items[next_id]
    next_id += 1
    return created

@app.get("/items/",response_model=list[Item])
def list_items():
    return list(items.values())


