from datetime import timedelta

from fastapi import HTTPException, status

from app.config import config
from app.user.application.services import UserService
from app.user.domain.entities import User, UserCreate
from app.user.domain.ports import UserPort


class UserAdapter(UserPort):
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def signup(self, user: UserCreate):
        db_user = self.user_service.retrieve_user(user.email)

        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = self.user_service.hash_password(user.password)
        user = User(email=user.email, hashed_password=hashed_password)
        return self.user_service.create_user(user)

    def login(self, user: UserCreate):
        db_user = self.user_service.authenticate_user(user)

        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.user_service.create_access_token(
            data={"sub": db_user.email}, expires_delta=access_token_expires
        )

        return {"access_token": access_token, "token_type": "bearer"}
