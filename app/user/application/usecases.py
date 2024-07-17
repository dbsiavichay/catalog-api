from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext


class HashPasswordUsecase:
    def __init__(self, crypt_context: CryptContext) -> None:
        self.crypt_context = crypt_context

    def execute(self, password: str) -> str:
        return self.crypt_context.hash(password)


class VerifyPasswordUsecase:
    def __init__(self, crypt_context: CryptContext) -> None:
        self.crypt_context = crypt_context

    def execute(self, plain_password: str, hashed_password) -> bool:
        return self.crypt_context.verify(plain_password, hashed_password)


class CreateAccessTokenUsecase:
    def __init__(self, secret_key: str, algorithm: str) -> None:
        self.secret_key = secret_key
        self.algorithm = algorithm

    def execute(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

        return encoded_jwt
