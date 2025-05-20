from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)


class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float

class ProductCreate(ProductBase):
    pass  # Keine zusätzlichen Felder erforderlich, daher leer

class ProductRead(ProductBase):
    id: int

    class Config:
        from_attributes = True
