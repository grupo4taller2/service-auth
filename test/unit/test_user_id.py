from src.domain.user_id import UserID


def test_user_id_creation():
    user_id = UserID(text='email@domain.com')
    assert user_id.text == 'email@domain.com'
