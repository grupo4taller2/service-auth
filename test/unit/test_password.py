from src.domain.password import Password


def test_password_creation():
    password = Password(text='some_password')
    assert password.text == 'some_password'
