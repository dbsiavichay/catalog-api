import boto3

from .catalog.infra.adapters import ProductAdapter
from .catalog.infra.repositories import DynamoDBClient, ProductRepositoryImpl
from .config import config

ddb_resource = boto3.resource(
    "dynamodb",
    region_name=config.AWS_REGION_NAME,
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    endpoint_url=config.AWS_ENDPOINT_URL,
)
ddb_client = DynamoDBClient(table_name="products", ddb_resource=ddb_resource)

product_repository = ProductRepositoryImpl(ddb_client)

product_adapter = ProductAdapter(product_repository)
