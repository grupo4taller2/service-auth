from pydantic import Field
from pydantic.main import BaseModel


class TipitoCreateRequest(BaseModel):
    name: str = Field(example="tipito's name")


class TipitoResponse(BaseModel):
    name: str = Field(example="tipito's name")
