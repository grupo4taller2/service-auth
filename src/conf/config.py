from pydantic import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    DATABASE_URI: str
    API_V1_STR: str = os.environ.get("API_VERSION_PREFIX")
    # TODO: Maybe move the following two to env vars?
    CRYPT_CONTEXT_SCHEME: List[str] = ['bcrypt']
    CRYPT_CONTEXT_DEPRECATED: str = 'auto'
    JWT_SECRET: str
    JWT_ALGORITHM: str
    # FIXME: Add JWT expiration date
