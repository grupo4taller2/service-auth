from __future__ import annotations

import abc
from src.adapters.repositories.credentials_base_repository \
    import CredentialsBaseRepository


class AbstractCredentialsUnitOfWork(abc.ABC):
    repository: CredentialsBaseRepository

    def __enter__(self) -> AbstractCredentialsUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def collect_new_events(self):
        for credentials in self.repository.seen:
            while credentials.events:
                yield credentials.events.pop(0)

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
