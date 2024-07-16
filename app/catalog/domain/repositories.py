from abc import ABC, abstractmethod

from .entities import Product


class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product):
        pass
