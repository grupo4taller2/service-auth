from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

from src.domain.credentials import Credentials
from src.domain.user_id import UserID
from src.domain.password import Password

Base = declarative_base()


class CredentialsDTO(Base):
    __tablename__ = "users"

    email: Union[str, Column] = Column(String, primary_key=True, index=True)
    hashed_password: Union[str, Column] = Column(String)

    @staticmethod
    def from_entity(c: Credentials) -> Credentials:
        return CredentialsDTO(
            email=c.uid.text,
            hashed_password=c.password.text
        )

    def to_entity(self) -> Credentials:
        user_id = UserID(text=self.email)
        password = Password(text=self.hashed_password)
        return Credentials(
            uid=user_id,
            password=password,
            events=[]
        )
