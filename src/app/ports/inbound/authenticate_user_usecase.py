from abc import ABC, abstractmethod
from pydantic.main import BaseModel
from pydantic import EmailStr


class AuthenticateUserCommand(BaseModel):
    email:    EmailStr
    password: str


class AuthenticateUserUseCase(ABC):

    @abstractmethod
    # TODO: Add type annotations for auto-completion
    def authenticateUser(command: AuthenticateUserCommand):
        pass
