from app.catalog.domain.entities import Product, ProductCreate, ProductUpdate
from app.catalog.domain.repositories import ProductRepository
from app.shared.infra.clients import DynamoDBClient


class ProductRepositoryImpl(ProductRepository):
    def __init__(self, ddb_client: DynamoDBClient) -> None:
        self.ddb_client = ddb_client

    def create(self, product: ProductCreate):
        self.ddb_client.put_item(product.model_dump())
        return product

    def retrieve(self, sku: str) -> Product:
        response = self.ddb_client.get_item({"sku": sku})
        item = response.get("Item")

        if item:
            return Product(**item)

        return None

    def update(self, sku: str, product: ProductUpdate) -> Product:
        response = self.ddb_client.update_item(
            key={"sku": sku}, update_values=product.model_dump(exclude_none=True)
        )

        item = response.get("Attributes")

        if item:
            return Product(**item)

        return None

    def update_queried(self, sku: str, queried_number: int):
        return self.ddb_client.update_item(
            key={"sku": sku}, update_values={"queried_by_anonymous": queried_number}
        )

    def delete(self, sku: str):
        self.ddb_client.delete_item(key={"sku": sku})
