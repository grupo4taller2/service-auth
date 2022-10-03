import abc
from typing import Optional
from src.domain.credentials import Credentials
from src.domain.validation_source import ValidationSource


class AbstractValidator(abc.ABC):
    validation_source: Optional[ValidationSource]

    @abc.abstractmethod
    def vlaidate(self, credentials: Credentials):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
