import abc
from src.domain.tipito import Tipito
from typing import Set


class TipitoBaseRepository(metaclass=abc.ABCMeta):
    def __init__(self):
        self.seen: Set[Tipito] = set()

    @abc.abstractmethod
    def save(self, tipito: Tipito):
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_name(self, name: str) -> Tipito:
        raise NotImplementedError
