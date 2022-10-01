from pydantic import BaseModel


class Event(BaseModel):
    pass


class TipitoCreatedEvent(Event):
    name: str
