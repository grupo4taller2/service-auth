from pydantic import BaseModel


class Command(BaseModel):
    pass


class TipitoCreateCommand(Command):
    name: str


class TipitoGetCommand(Command):
    name: str
