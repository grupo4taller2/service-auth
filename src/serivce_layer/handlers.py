from src.domain.commands import (
    TipitoCreateCommand,
    TipitoGetCommand
)
from src.domain.events import (
    TipitoCreatedEvent
)

from src.serivce_layer.abstract_unit_of_work import AbstractTipitoUnitOfWork

from src.domain.tipito import Tipito


def get_tipito(cmd: TipitoGetCommand, uow: AbstractTipitoUnitOfWork):
    # FIXME: THROW IF NOT EXISTS
    with uow:
        tipito = uow.repository.find_by_name(name=cmd.name)
        uow.commit()
        return tipito


def create_tipito(cmd: TipitoCreateCommand, uow: AbstractTipitoUnitOfWork):
    with uow:
        tipito = uow.repository.find_by_name(name=cmd.name)
        # FIXME: Throw if tipito exists
        if tipito is None:
            tipito = Tipito(name=cmd.name)
            uow.repository.save(tipito)
        uow.commit()
        return tipito


def publish_created_event(event: TipitoCreatedEvent,
                          uow: AbstractTipitoUnitOfWork):
    print(f'Created event {event}')
