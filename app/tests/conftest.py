from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists

from app.core.dependencies import get_db
from app.db import Base
from app.main import app

from .utils.overrides import override_get_db
from .utils.test_db import SQLALCHEMY_DATABASE_URL, TestingSessionLocal, engine

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session")
def db() -> Generator:
    if not database_exists(SQLALCHEMY_DATABASE_URL):
        create_database(SQLALCHEMY_DATABASE_URL)

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    yield TestingSessionLocal()


@pytest.fixture(scope='function')
def db_session(db: Session) -> Generator:
    db.begin_nested()

    yield db

    db.rollback()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
