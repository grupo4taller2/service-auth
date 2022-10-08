from pydantic import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    DATABASE_URI: str = os.environ.get("DATABASE_URI")
    API_V1_STR: str = os.environ.get("API_VERSION_PREFIX")
    # TODO: Maybe move the following two to env vars?
    CRYPT_CONTEXT_SCHEME: List[str] = ['bcrypt']
    CRYPT_CONTEXT_DEPRECATED: str = 'auto'
    JWT_SECRET: str = os.environ.get("JWT_ALGORITHM")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM")
    # FIXME: Add JWT expiration date
