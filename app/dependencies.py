import boto3
from passlib.context import CryptContext

from .catalog.infra.adapters import ProductAdapter
from .catalog.infra.repositories import DynamoDBClient, ProductRepositoryImpl
from .config import config
from .user.application.services import UserService
from .user.application.usecases import (
    CreateAccessTokenUsecase,
    HashPasswordUsecase,
    VerifyPasswordUsecase,
)
from .user.infra.adapters import UserAdapter
from .user.infra.repositories import UserRepositoryImpl

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ddb_resource = boto3.resource(
    "dynamodb",
    region_name=config.AWS_REGION_NAME,
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    endpoint_url=config.AWS_ENDPOINT_URL,
)
ddb_products = DynamoDBClient(table_name="products", ddb_resource=ddb_resource)
ddb_users = DynamoDBClient(table_name="users", ddb_resource=ddb_resource)

product_repository = ProductRepositoryImpl(ddb_products)
user_repository = UserRepositoryImpl(ddb_users)

hash_password_usecase = HashPasswordUsecase(crypt_context)
verify_password_usecase = VerifyPasswordUsecase(crypt_context)
create_access_token_usecase = CreateAccessTokenUsecase(
    config.JWT_SECRET_KEY, config.JWT_ALGORITHM
)

user_service = UserService(
    hash_password_usecase,
    verify_password_usecase,
    create_access_token_usecase,
    user_repository,
)

product_port = ProductAdapter(product_repository)
user_port = UserAdapter(user_service)
