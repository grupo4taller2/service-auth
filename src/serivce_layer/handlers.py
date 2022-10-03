from src.domain.commands import (
    UserLoginCommand
)
from src.domain.events import (
    UserLoggedEvent
)

from src.serivce_layer.abstract_unit_of_work \
    import AbstractCredentialsUnitOfWork


def get_token(cmd: UserLoginCommand,
              uow: AbstractCredentialsUnitOfWork):
    with uow:
        true_creds = uow.repository.find_by_email(email=cmd.email)
        # FIXME: Do something if not existent
    # TODO: Here goes magic


def publish_created_event(event: UserLoggedEvent,
                          uow: AbstractCredentialsUnitOfWork):
    print(f'Created event {event}')
