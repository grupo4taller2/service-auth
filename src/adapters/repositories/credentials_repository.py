from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.adapters.repositories.credentials_base_repository \
    import CredentialsBaseRepository
from src.domain.credentials import Credentials
from src.adapters.repositories.credentials_dto import CredentialsDTO


class CredentialsRepository(CredentialsBaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def find_by_email(self, email: str) -> Credentials:
        try:
            creds_dto = self.session.query(CredentialsDTO) \
                .filter_by(email=email).one()
        except NoResultFound:
            # FIXME: Improve behaviour
            return None
        except Exception:
            raise
        creds = creds_dto.to_entity()
        self.seen.add(creds)
        return creds
