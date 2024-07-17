import jwt

from app.user.application.usecases import CreateAccessTokenUsecase


class TestCreateAccessTokenUsecase:
    def test_jwt_default_expiration(self):
        secret_key = "test_secret"
        algorithm = "HS256"
        usecase = CreateAccessTokenUsecase(secret_key, algorithm)
        data = {"user_id": 1}

        token = usecase.execute(data)
        decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])

        assert "exp" in decoded_token
        assert decoded_token["user_id"] == 1

    def test_empty_data_dictionary(self):
        secret_key = "test_secret"
        algorithm = "HS256"
        usecase = CreateAccessTokenUsecase(secret_key, algorithm)
        data = {}

        token = usecase.execute(data)
        decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])

        assert "exp" in decoded_token
        assert len(decoded_token) == 1  # Only 'exp' should be present in the token
