from ..db.base import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
