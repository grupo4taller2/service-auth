from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    DATABASE_URI: str
    API_V1_STR: str = "/api/v1"
    # TODO: Maybe move the following two to env vars?
    CRYPT_CONTEXT_SCHEME: List[str] = ['bcrypt']
    CRYPT_CONTEXT_DEPRECATED: str = 'auto'
    JWT_SECRET: str
    JWT_ALGORITHM: str
    # FIXME: Add JWT expiration date
