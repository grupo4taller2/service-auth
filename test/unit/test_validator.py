from src.domain.credentials import Credentials
from src.domain.password import Password
from src.domain.user_id import UserID
from src.domain.validator import DummyValidator, Validator
from src.domain.password_encoder import ByCryptPasswordEncoder


def test_validation_of_dummy_credentials():
    creds = Credentials(uid=UserID(text='email@domain.com'),
                        password=Password(text='secret'))
    validator = DummyValidator()
    assert validator.are_valid(creds, creds)


def test_validation_true_credentials():
    creds = Credentials(uid=UserID(text='email@domain.com'),
                        password=Password(text='secret'))
    encoder = ByCryptPasswordEncoder()
    validator = Validator(encoder)
    hashed_password = encoder.encode('secret')
    stored_credentials = Credentials(uid=UserID(text='email@domain.com'),
                                     password=Password(text=hashed_password))

    assert validator.are_valid(creds, stored_credentials)
