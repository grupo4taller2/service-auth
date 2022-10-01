from __future__ import annotations

import abc
from src.adapters.repositories.tipito_base_repository \
    import TipitoBaseRepository


class AbstractTipitoUnitOfWork(abc.ABC):
    repository: TipitoBaseRepository

    def __enter__(self) -> AbstractTipitoUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def collect_new_events(self):
        for tipito in self.repository.seen:
            while tipito.events:
                yield tipito.events.pop(0)

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
