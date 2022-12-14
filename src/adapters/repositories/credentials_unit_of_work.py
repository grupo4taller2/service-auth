from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.adapters.repositories.credentials_repository \
    import CredentialsRepository
from src.serivce_layer.abstract_unit_of_work \
    import AbstractCredentialsUnitOfWork

from src.conf import config


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.Settings().DATABASE_URI,
        isolation_level="REPEATABLE READ",
    )
)


class CredentialsUnitOfWork(AbstractCredentialsUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.repository = CredentialsRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
