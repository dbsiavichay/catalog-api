from datetime import timedelta
from typing import Optional

from app.user.domain.entities import User, UserCreate
from app.user.domain.repositories import UserRepository

from .usecases import (
    CreateAccessTokenUsecase,
    HashPasswordUsecase,
    VerifyPasswordUsecase,
)


class UserService:
    def __init__(
        self,
        hash_pw_usecase: HashPasswordUsecase,
        verify_pw_usecase: VerifyPasswordUsecase,
        create_access_token_usecase: CreateAccessTokenUsecase,
        user_repository: UserRepository,
    ) -> None:
        self.hash_pw_usecase = hash_pw_usecase
        self.verify_pw_usecase = verify_pw_usecase
        self.create_access_token_usecase = create_access_token_usecase
        self.user_repository = user_repository

    def hash_password(self, password: str) -> str:
        return self.hash_pw_usecase.execute(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.verify_pw_usecase.execute(plain_password, hashed_password)

    def retrieve_user(self, email: str) -> User:
        return self.user_repository.retrieve(email)

    def create_user(self, user: User) -> User:
        return self.user_repository.create(user)

    def authenticate_user(self, user: UserCreate) -> Optional[User]:
        db_user = self.retrieve_user(user.email)

        if not db_user:
            return None
        if not self.verify_password(user.password, db_user.hashed_password):
            return None

        return db_user

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        return self.create_access_token_usecase.execute(data, expires_delta)
