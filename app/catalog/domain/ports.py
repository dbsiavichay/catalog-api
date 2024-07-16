from abc import ABC, abstractmethod

from .entities import Product


class ProductPort(ABC):
    @abstractmethod
    def create(self, product: Product):
        pass
