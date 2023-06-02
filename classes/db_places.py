from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from db_base import Base


class Places(Base):
    __tablename__ = "places"

    headers = {'id': 'ID',
               'name': 'Место учёбы',
               'comment': 'Комментарий',
               'smena': 'Смена'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(200), nullable=True)
    comment: Mapped[str] = Column(String(20), nullable=True)
    smena: Mapped[int] = Column(Integer())

    zregister = relationship("Zregister", back_populates="places")
