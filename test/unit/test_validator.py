from src.domain.credentials import Credentials
from src.domain.password import Password
from src.domain.user_id import UserID
from src.domain.validator import DummyValidator


def test_validation_of_dummy_credentials():
    creds = Credentials(uid=UserID(text='email@domain.com'),
                        password=Password(text='secret'))
    validator = DummyValidator(user_id='email@domain.com',
                               password='secret')
    assert validator.validate(creds)
