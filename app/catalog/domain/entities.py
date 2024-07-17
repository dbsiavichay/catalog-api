from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    sku: str
    name: str
    price: Decimal = 0
    brand: Optional[str]
    queried_by_anonymous: int = 0


class ProductCreate(BaseModel):
    sku: str
    name: str
    price: Decimal = 0
    brand: Optional[str]


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[Decimal] = None
    brand: Optional[str] = None
