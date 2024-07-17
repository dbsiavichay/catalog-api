import pytest
from fastapi import HTTPException

from app.user.application.services import UserService
from app.user.domain.entities import User, UserCreate
from app.user.infra.adapters import UserAdapter


class TestUserAdapter:
    def test_signup_success(self, mocker):
        user_service_mock = mocker.Mock(spec=UserService)
        user_service_mock.retrieve_user.return_value = None
        user_service_mock.hash_password.return_value = "hashed_password"
        user_service_mock.create_user.return_value = User(
            email="test@example.com", hashed_password="hashed_password"
        )

        user_adapter = UserAdapter(user_service=user_service_mock)
        user_create = UserCreate(email="test@example.com", password="password")

        result = user_adapter.signup(user_create)

        assert result.email == "test@example.com"
        assert result.hashed_password == "hashed_password"

    def test_signup_existing_email_raises_http_400(self, mocker):
        user_service_mock = mocker.Mock(spec=UserService)
        user_service_mock.retrieve_user.return_value = User(
            email="test@example.com", hashed_password="hashed_password"
        )

        user_adapter = UserAdapter(user_service=user_service_mock)
        user_create = UserCreate(email="test@example.com", password="password")

        with pytest.raises(HTTPException) as exc_info:
            user_adapter.signup(user_create)

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Email already registered"
