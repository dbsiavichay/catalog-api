from abc import ABC, abstractmethod

from .entities import Product


class ProductPort(ABC):
    @abstractmethod
    def create(self, product: Product):
        pass

    @abstractmethod
    def retrieve(self, sku: str):
        pass

    @abstractmethod
    def update(self, sku: str, product: Product):
        pass

    @abstractmethod
    def delete(self, sku: str):
        pass
