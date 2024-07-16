from app.catalog.domain.entities import Product
from app.catalog.domain.ports import ProductPort
from app.catalog.domain.repositories import ProductRepository


class ProductAdapter(ProductPort):
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def create(self, product: Product):
        return self.product_repository.create(product)
