from __future__ import annotations
from typing import Union

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

from src.domain.tipito import Tipito

Base = declarative_base()


class TipitoDTO(Base):
    __tablename__ = "tipitos"

    name: Union[str, Column] = Column(String, primary_key=True, index=True)
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), onupdate=func.now()
    )

    @staticmethod
    def from_entity(tipito: Tipito) -> TipitoDTO:
        return TipitoDTO(
            name=tipito.name,
        )

    def to_entity(self) -> Tipito:
        return Tipito(
            name=self.name,
            events=[]
        )
