from src.domain.credentials import Credentials
from src.domain.password import Password
from src.domain.user_id import UserID


def test_credentials_creation():
    credentials = Credentials(uid=UserID(text='email@domain.com'),
                              password=Password(text='secret'))
    assert credentials.uid == UserID(text='email@domain.com') \
        and credentials.password == Password(text='secret')
