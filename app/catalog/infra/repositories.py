from app.catalog.domain.entities import Product
from app.catalog.domain.repositories import ProductRepository
from app.shared.infra.clients import DynamoDBClient


class ProductRepositoryImpl(ProductRepository):
    def __init__(self, ddb_client: DynamoDBClient) -> None:
        self.ddb_client = ddb_client

    def create(self, product: Product):
        self.ddb_client.put_item(product.model_dump())
        return product

    def retrieve(self, sku: str):
        response = self.ddb_client.get_item({"sku": sku})
        return response.get("Item")

    def update(self, sku: str, product: Product):
        return self.ddb_client.update_item(
            key={"sku": sku}, update_values=product.model_dump(exclude_none=True)
        )

    def delete(self, sku: str):
        self.ddb_client.delete_item(key={"sku": sku})
