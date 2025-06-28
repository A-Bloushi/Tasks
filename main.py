from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel



class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id:int, detail: Optional[str] = None):
#     response =  {"item_id": item_id}
#     if detail:
#         response["detail"] = detail
#     return response


@app.post("/items/")
def create_item(item:Item):
    return item.description + "test"
