from typing import Annotated

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError

from app.config import config
from app.dependencies import user_port
from app.user.domain.entities import Token, User, UserCreate

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM]
        )
        email: str = payload.get("sub")

        if not email:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception

    user = user_port.user_service.retrieve_user(email)

    if not user:
        raise credentials_exception

    return user


async def get_current_user_optional(token: Annotated[str, Depends(oauth2_scheme)]):
    if not token:
        return None

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM]
        )
        email: str = payload.get("sub")

        if not email:
            return None

    except InvalidTokenError:
        raise credentials_exception

    user = user_port.user_service.retrieve_user(email)

    if not user:
        raise credentials_exception

    return user


@router.post("/register", response_model=User)
def register(user: UserCreate):
    return user_port.signup(user)


@router.post("/login", response_model=Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return user_port.login(
        UserCreate(email=form_data.username, password=form_data.password)
    )
