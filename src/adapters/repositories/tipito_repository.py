from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.adapters.repositories.tipito_base_repository \
    import TipitoBaseRepository
from src.domain.tipito import Tipito
from src.adapters.repositories.tipito_dto import TipitoDTO


class TipitoRepository(TipitoBaseRepository):
    def __init__(self, session):
        super().__init__()
        self.session: Session = session

    def save(self, tipito: Tipito):
        tipito_dto = TipitoDTO.from_entity(tipito)
        try:
            self.session.add(tipito_dto)
            self.seen.add(tipito)
        except Exception:
            raise

    def find_by_name(self, name: str) -> Tipito:
        try:
            tipito_dto = self.session.query(TipitoDTO) \
                .filter_by(name=name).one()
        except NoResultFound:
            return None
        except Exception:
            raise
        tipito = tipito_dto.to_entity()
        self.seen.add(tipito)
        return tipito
