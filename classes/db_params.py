from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from db_base import Base


class Params(Base):
    __tablename__ = "params"

    headers = {'id': 'ID',
               'name': 'Наим.',
               'data': 'Знач.'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(50), nullable=True)
    data: Mapped[str] = Column(String(50), nullable=True)
