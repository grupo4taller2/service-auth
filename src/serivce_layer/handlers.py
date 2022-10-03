from datetime import datetime

from src.domain.commands import (
    UserLoginCommand
)
from src.domain.events import (
    UserLoggedEvent
)

from src.conf.config import Settings

from src.serivce_layer.abstract_unit_of_work \
    import AbstractCredentialsUnitOfWork

from src.domain.credentials import Credentials
from src.domain.password import Password
from src.domain.user_id import UserID
from src.domain.validator import Validator
from src.domain.password_encoder import ByCryptPasswordEncoder
from src.domain.token_generator import TokenGenerator

def get_token(cmd: UserLoginCommand,
              uow: AbstractCredentialsUnitOfWork):
    with uow:
        true_creds = uow.repository.find_by_email(email=cmd.email)
        # FIXME: Do something if not existent
    # TODO: Here goes magic
    # Do actual authentication or throw?
    given_creds = Credentials(uid=UserID(text=cmd.email),
                              password=Password(text=cmd.password))
    validator = Validator(ByCryptPasswordEncoder())
    if not validator.are_valid(given_creds, true_creds):
        # FIXME: raise exception
        pass

    key = Settings().JWT_SECRET
    algorithm = Settings().JWT_ALGORITHM
    generator = TokenGenerator(key, algorithm)
    date = datetime.utcnow()

    return generator.create_access_token(cmd.email, date)
    

def publish_created_event(event: UserLoggedEvent,
                          uow: AbstractCredentialsUnitOfWork):
    print(f'Created event {event}')
