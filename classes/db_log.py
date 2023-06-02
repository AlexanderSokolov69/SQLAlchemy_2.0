from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from db_base import Base


class Log(Base):
    __tablename__ = "log"

    headers = {'id': 'ID',
               'name': 'Name',
               'date': 'Date',
               'time': 'Time',
               'info': 'Info',
               'uid': 'UID'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(4), nullable=True)
    date: Mapped[date] = Column(String(20), nullable=True)
    time: Mapped[str] = Column(String(20), nullable=True)
    info: Mapped[str] = Column(String(200), nullable=True)
    uid: Mapped[str] = Column(String(10), nullable=True)
