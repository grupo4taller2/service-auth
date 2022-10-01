from typing import List, Optional
from pydantic import BaseModel

from src.domain.events import Event


class Tipito(BaseModel):
    name: str
    events: Optional[List[Event]]

    class Config:
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name
