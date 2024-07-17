from app.shared.infra.clients import DynamoDBClient
from app.user.domain.entities import User
from app.user.domain.repositories import UserRepository


class UserRepositoryImpl(UserRepository):
    def __init__(self, ddb_client: DynamoDBClient) -> None:
        self.ddb_client = ddb_client

    def create(self, user: User):
        self.ddb_client.put_item(user.model_dump())
        return user

    def retrieve(self, email: str) -> User:
        response = self.ddb_client.get_item({"email": email})
        dict_user = response.get("Item")

        if dict_user:
            return User(**dict_user)

        return None
