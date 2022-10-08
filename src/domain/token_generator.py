from jose import jwt
from src.conf.config import Settings
from datetime import datetime, timedelta


class TokenGenerator:
    def __init__(self,
                 secret_key: str,
                 algorithm: str,
                 duration_in_minutes: int = 15):
        self.secret_key = Settings().JWT_SECRET
        self.algorithm = Settings().JWT_ALGORITHM
        self.duration_in_minutes = duration_in_minutes

    def create_access_token(self,
                            username: str,
                            date: datetime):
        expiration = date + timedelta(minutes=self.duration_in_minutes)
        to_encode = {
            'sub': username,
            'exp': expiration
        }
        return jwt.encode(to_encode, self.secret_key, self.algorithm)
