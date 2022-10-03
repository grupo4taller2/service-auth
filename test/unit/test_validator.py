from src.domain.credentials import Credentials
from src.domain.password import Password
from src.domain.user_id import UserID


def test_validation_of_correct_credentials():
    creds = Credentials(uid=UserID(text='email@domain.com'),
                        password=Password(text='secret'))
    validator = DummyValidator(None)
    assert validator.validate(creds)
