from app.catalog.domain.entities import Product, UpdatedProduct
from app.catalog.domain.ports import ProductPort
from app.catalog.domain.repositories import ProductRepository


class ProductAdapter(ProductPort):
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def create(self, product: Product):
        return self.product_repository.create(product)

    def retrieve(self, sku: str):
        return self.product_repository.retrieve(sku=sku)

    def update(self, sku: str, product: UpdatedProduct):
        return self.product_repository.update(sku=sku, product=product)
