import abc
from passlib.context import CryptContext
from src.conf.config import Settings


class PasswordEncoder(abc.ABC):
    @abc.abstractmethod
    def encode(self, text: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def verify(self, given_pwd, true_hashed_pwd) -> bool:
        raise NotImplementedError


class ByCryptPasswordEncoder(PasswordEncoder):
    def __init__(self):
        self.context = CryptContext(
            schemes=Settings().CRYPT_CONTEXT_SCHEME,
            deprecated=Settings().CRYPT_CONTEXT_DEPRECATED)

    def encode(self, text: str) -> str:
        return self.context.hash(text)

    def verify(self, given_pwd, true_hashed_pwd) -> bool:
        return self.context.verify(given_pwd, true_hashed_pwd)
