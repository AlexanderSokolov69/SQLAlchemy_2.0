from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from db_base import Base


class Kabs(Base):
    __tablename__ = "kabs"

    headers = {'id': 'ID',
               'name': '№каб',
               'color': 'Цвет каб.'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(4), nullable=True)
    color: Mapped[str] = Column(String(20), nullable=True)

    rasp = relationship("Rasp", back_populates="kabs")