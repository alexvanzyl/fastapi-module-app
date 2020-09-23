from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from app.config import settings
from tests.utils.user import create_random_user, random_lower_string


def test_getting_token(client: TestClient, db: Session) -> None:
    plain_password = random_lower_string()
    user = create_random_user(db, password=plain_password)
    login_data = {
        'username': user.email,
        'password': plain_password
    }
    r = client.post(f'{settings.API_V1_STR}/auth/token', data=login_data)

    response = r.json()
    assert r.status_code == HTTP_200_OK
    assert 'access_token' in response
    assert response['access_token']


def test_getting_token_with_invalid_credentials(client: TestClient) -> None:
    login_data = {
        'username': 'invalid-user',
        'password': 'invalid-user'
    }

    r = client.post(f'{settings.API_V1_STR}/auth/token', data=login_data)

    response = r.json()
    assert r.status_code == HTTP_400_BAD_REQUEST
    assert 'detail' in response
