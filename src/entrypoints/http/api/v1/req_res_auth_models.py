from pydantic import Field
from pydantic.main import BaseModel


class UserLoginRequest(BaseModel):
    email: str = Field(example="email@domain.com")
    password: str = Field(example='plain_password')


class TokenResponse(BaseModel):
    token: str = Field(example="X.Y.Z")
    token_type: str = Field(example='bearer')
