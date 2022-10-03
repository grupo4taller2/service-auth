import abc
from src.domain.credentials import Credentials
from typing import Set


class CredentialsBaseRepository(metaclass=abc.ABCMeta):
    def __init__(self):
        self.seen: Set[Credentials] = set()

    @abc.abstractmethod
    def find_by_email(self, email: str) -> Credentials:
        raise NotImplementedError
