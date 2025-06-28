from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database import engine, Base, get_db
from sqlalchemy.ext.asyncio import AsyncSession
from models import ItemModel
from fastapi import Depends
from sqlalchemy.future import select

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

items: dict[int, Item] = {}
next_id = 1



@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs before the app starts
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # This runs when the app shuts down (optional)
    # You could close connections here if needed

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item, db: AsyncSession = Depends(get_db)):
    new_item = ItemModel(
        name=item.name,
        description=item.description,
        price=item.price,
        tax=item.tax
    )
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item


@app.get("/items/", response_model=list[Item])
async def list_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ItemModel))
    items = result.scalars().all()
    return items