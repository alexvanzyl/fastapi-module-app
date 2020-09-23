from uuid import uuid4

from jose import jwt

from app.config import settings
from app.core.security import (ALGORITHM, create_access_token,
                               get_hashed_password, verify_password)


def test_get_hashed_password():
    plain_password = 'password'
    hashed_password = get_hashed_password(plain_password)

    assert hashed_password
    assert hashed_password != plain_password


def test_verify_password():
    plain_password = 'password'
    hashed_password = get_hashed_password(plain_password)

    assert verify_password(hashed_password, plain_password)


def test_create_access_token():
    fake_user_id = uuid4()
    token = create_access_token(subject=fake_user_id)
    claims = jwt.decode(token, key=settings.SECRET_KEY, algorithms=ALGORITHM)

    assert claims
    assert 'sub' in claims
    assert claims['sub'] == str(fake_user_id)
