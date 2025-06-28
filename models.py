from sqlalchemy import Column, Integer, String, Float, Text
from database import Base

# ItemModel represents an item in the inventory system.
class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)

