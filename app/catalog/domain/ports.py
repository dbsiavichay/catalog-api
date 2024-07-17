from abc import ABC, abstractmethod
from typing import Optional

from app.user.domain.entities import User

from .entities import ProductCreate, ProductUpdate


class ProductPort(ABC):
    @abstractmethod
    def create(self, product: ProductCreate):
        pass

    @abstractmethod
    def retrieve(self, sku: str, user: Optional[User]):
        pass

    @abstractmethod
    def update(self, sku: str, product: ProductUpdate):
        pass

    @abstractmethod
    def delete(self, sku: str):
        pass
