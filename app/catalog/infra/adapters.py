from typing import Optional

from app.catalog.domain.entities import ProductCreate, ProductUpdate
from app.catalog.domain.ports import ProductPort
from app.catalog.domain.repositories import ProductRepository
from app.user.domain.entities import User


class ProductAdapter(ProductPort):
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def create(self, product: ProductCreate):
        return self.product_repository.create(product)

    def retrieve(self, sku: str, user: Optional[User]):
        product = self.product_repository.retrieve(sku=sku)

        if product and not user:
            self.product_repository.update_queried(
                sku, product.queried_by_anonymous + 1
            )

        return product

    def update(self, sku: str, product: ProductUpdate):
        return self.product_repository.update(sku=sku, product=product)

    def delete(self, sku: str):
        return self.product_repository.delete(sku=sku)
