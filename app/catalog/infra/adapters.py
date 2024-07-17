from typing import Optional

from app.catalog.domain.entities import ProductCreate, ProductUpdate
from app.catalog.domain.ports import ProductPort
from app.catalog.domain.repositories import ProductRepository
from app.config import config
from app.shared.domain.entities import Email
from app.shared.domain.ports import EmailPort
from app.user.domain.entities import User


class ProductAdapter(ProductPort):
    def __init__(
        self, product_repository: ProductRepository, email_port: EmailPort
    ) -> None:
        self.product_repository = product_repository
        self.email_port = email_port

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
        product = self.product_repository.update(sku=sku, product=product)

        email = Email(
            sender="hello@example.com",
            recipients=config.ADMINS,
            subject="Product Updated",
            body_text=f"Product {product.name} with {product.sku} has been updated.",
        )
        self.email_port.send_email(email)

        return product

    def delete(self, sku: str):
        return self.product_repository.delete(sku=sku)
