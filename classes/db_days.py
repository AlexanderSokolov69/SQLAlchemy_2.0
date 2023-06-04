from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from .db_base import Base


class Days(Base):
    __tablename__ = "days"

    headers = {'id': 'ID',
               'name': 'День',
               'cname': 'Наименование'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(15), nullable=True)
    cname: Mapped[str] = Column(String(5), nullable=True)

    rasp = relationship("Rasp", back_populates="days")