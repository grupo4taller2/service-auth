from pydantic import BaseModel

from src.domain.password import Password
from src.domain.user_id import UserID


class Credentials(BaseModel):
    uid: UserID
    password: Password

    class Config:
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.uid.text + self.password.text)

    def __eq__(self, other):
        return self.uid == other.uid and self.password == other.password
