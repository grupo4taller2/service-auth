from typing import Protocol


class User:
    def __init__(self, name):
        self.name = name


class Email:
    def __init__(self, email_address):
        self.address = email_address


class UserRepository(Protocol):
    def get(self, identifier: Email) -> User:
        ...


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session):
        self.session = session
    
    def get(self, email: Email) -> User:
        if email.address == 'macalvo@fi.uba.ar':
            return User('Mateo')
        return User('Desconocido')
