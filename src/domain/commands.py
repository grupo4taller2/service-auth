from pydantic import BaseModel


class Command(BaseModel):
    pass


class UserLoginCommand(Command):
    email: str
    password: str
