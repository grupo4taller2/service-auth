import abc
from typing import Optional
from pydantic import BaseModel
from src.domain.credentials import Credentials
from src.domain.validation_source import ValidationSource


class AbstractValidator(abc.ABC, BaseModel):
    validation_source: Optional[ValidationSource]

    class Config:
        arbitrary_types_allowed = True

    @abc.abstractmethod
    def validate(self, credentials: Credentials):
        raise NotImplementedError


class DummyValidator(AbstractValidator):
    user_id: str
    password: str

    def validate(self, credentials: Credentials):
        return credentials.uid.text == self.user_id \
            and credentials.password.text == self.password
