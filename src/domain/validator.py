import abc
from src.domain.credentials import Credentials
from src.domain.password_encoder import PasswordEncoder


class AbstractValidator(abc.ABC):
    @abc.abstractmethod
    def are_valid(self,
                  given: Credentials,
                  ground_truth: Credentials) -> bool:
        raise NotImplementedError


class DummyValidator(AbstractValidator):
    def are_valid(self,
                  given: Credentials,
                  ground_truth: Credentials) -> bool:
        return True


class Validator(AbstractValidator):
    def __init__(self, encoder: PasswordEncoder):
        self.encoder = encoder

    def are_valid(self,
                  given: Credentials,
                  ground_truth: Credentials) -> bool:
        given_pwd = given.password.text
        true_hashed_pwd = ground_truth.password.text
        same_password = self.encoder.verify(given_pwd, true_hashed_pwd)
        same_id = (given.uid.text == ground_truth.uid.text)
        return (same_id and same_password)
