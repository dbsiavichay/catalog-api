import logging

from botocore.exceptions import ClientError

from app.catalog.domain.entities import Product
from app.catalog.domain.repositories import ProductRepository

logger = logging.getLogger(__name__)


class DynamoDBClient:
    def __init__(self, table_name, ddb_resource):
        self.table_name = table_name
        self.table = ddb_resource.Table(table_name)

    def put_item(self, item):
        try:
            self.table.put_item(Item=item)
            return item
        except ClientError as e:
            logger.exception(e.response["Error"]["Message"])
            raise

    def get_item(self, key):
        try:
            response = self.table.get_item(Key=key)
            return response.get("Item")
        except ClientError as e:
            logger.exception(e.response["Error"]["Message"])
            raise

    def update_item(self, key, update_values):
        update_expression = "SET " + ", ".join(
            f"#{k} = :{k}" for k in update_values.keys()
        )
        expression_attribute_values = {f":{k}": v for k, v in update_values.items()}
        expression_attribute_names = {f"#{k}": k for k in update_values.keys()}

        try:
            response = self.table.update_item(
                Key=key,
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ExpressionAttributeNames=expression_attribute_names,
                ReturnValues="ALL_NEW",
            )
            return response.get("Attributes")
        except ClientError as e:
            logger.exception(e.response["Error"]["Message"])
            raise

    def delete_item(self, key):
        try:
            response = self.table.delete_item(Key=key)
            return response
        except ClientError as e:
            logger.exception(e.response["Error"]["Message"])
            raise


class ProductRepositoryImpl(ProductRepository):
    def __init__(self, ddb_client: DynamoDBClient) -> None:
        self.ddb_client = ddb_client

    def create(self, product: Product):
        return self.ddb_client.put_item(product.model_dump())

    def retrieve(self, sku: str):
        return self.ddb_client.get_item({"sku": sku})

    def update(self, sku: str, product: Product):
        return self.ddb_client.update_item(
            key={"sku": sku}, update_values=product.model_dump(exclude_none=True)
        )

    def delete(self, sku: str):
        self.ddb_client.delete_item(key={"sku": sku})
