from botocore.exceptions import ClientError

from app.catalog.domain.entities import Product
from app.catalog.domain.repositories import ProductRepository


class DynamoDBClient:
    def __init__(self, table_name, ddb_resource):
        self.table_name = table_name
        # self.ddb = ddb_resource
        self.table = ddb_resource.Table(table_name)

    def put_item(self, item):
        try:
            self.table.put_item(Item=item)
            return item
        except ClientError as e:
            print(e.response["Error"]["Message"])
            raise

    def read_item(self, key):
        try:
            response = self.table.get_item(Key=key)
            return response.get("Item")
        except ClientError as e:
            print(e.response["Error"]["Message"])
            return None

    def update_item(self, key, update_expression, expression_attribute_values):
        try:
            response = self.table.update_item(
                Key=key,
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="UPDATED_NEW",
            )
            return response
        except ClientError as e:
            print(e.response["Error"]["Message"])
            return None

    def delete_item(self, key):
        try:
            response = self.table.delete_item(Key=key)
            return response
        except ClientError as e:
            print(e.response["Error"]["Message"])
            return None


class ProductRepositoryImpl(ProductRepository):
    def __init__(self, ddb_client: DynamoDBClient) -> None:
        self.ddb_client = ddb_client

    def create(self, product: Product):
        return self.ddb_client.put_item(product.model_dump())
