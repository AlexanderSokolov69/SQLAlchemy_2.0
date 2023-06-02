from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from db_base import Base


class Monts(Base):
    __tablename__ = "monts"

    headers = {'id': 'ID',
               'num': 'Ном.',
               'name': 'Месяц'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    num: Mapped[str] = Column(Integer(), nullable=True)
    name: Mapped[str] = Column(String(20), nullable=True)
