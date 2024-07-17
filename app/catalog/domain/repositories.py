from abc import ABC, abstractmethod

from .entities import Product, ProductCreate, ProductUpdate


class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: ProductCreate):
        pass

    @abstractmethod
    def retrieve(self, sku: str) -> Product:
        pass

    @abstractmethod
    def update(self, sku: str, product: ProductUpdate):
        pass

    @abstractmethod
    def update_queried(self, sku: str, queried_number: int):
        pass

    @abstractmethod
    def delete(self, sku: str):
        pass
