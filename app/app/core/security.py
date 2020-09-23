from datetime import datetime, timedelta, timezone

from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
from jose import jwt

from typing import Any, Union

from ..config import settings

password_hasher = PasswordHasher()

ALGORITHM = "HS256"


def get_hashed_password(password: str) -> str:
    return password_hasher.hash(password)


def verify_password(hashed_password: str, plain_password: str) -> bool:
    try:
        password_hasher.verify(hashed_password, plain_password)
    except VerificationError:
        return False
    return True


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {'exp': expire, 'sub': str(subject)}
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
