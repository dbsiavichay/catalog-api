import logging

from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class DynamoDBClient:
    def __init__(self, table_name, ddb_resource):
        self.table_name = table_name
        self.table = ddb_resource.Table(table_name)

    def put_item(self, item):
        try:
            return self.table.put_item(Item=item)
        except ClientError as e:
            logger.exception(e.response["Error"]["Message"])
            raise

    def get_item(self, key):
        try:
            return self.table.get_item(Key=key)
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
            return response
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
