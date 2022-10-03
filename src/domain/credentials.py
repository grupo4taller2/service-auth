from pydantic import BaseModel
from typing import Optional, List

from src.domain.password import Password
from src.domain.events import Event
from src.domain.user_id import UserID


class Credentials(BaseModel):
    uid: UserID
    password: Password
    events: Optional[List[Event]]

    class Config:
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.uid.text + self.password.text)

    def __eq__(self, other):
        return self.uid == other.uid and self.password == other.password
