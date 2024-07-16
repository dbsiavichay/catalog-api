from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    sku: str
    name: str
    price: Decimal = 0
    brand: Optional[str]


class UpdatedProduct(BaseModel):
    name: str
    price: Decimal = 0
    brand: Optional[str]
