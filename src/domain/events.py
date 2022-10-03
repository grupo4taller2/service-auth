from pydantic import BaseModel


class Event(BaseModel):
    pass


class UserLoggedEvent(Event):
    name: str
