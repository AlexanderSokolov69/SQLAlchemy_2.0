from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date

from db_base import Base


class Rasp(Base):
    __tablename__ = "rasp"

    headers = {'id': 'ID',
               'idGroups': 'ID Группы',
               'idKabs': 'ID Кабинета',
               'tstart': 'Начало',
               'tend': 'Окончание',
               'comment': 'Доп. информация',
               'name': 'Название',
               'idDays': 'ID Дня'
               }
    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    idGroups: Mapped[int] = Column(Integer(), ForeignKey("groups.id"))
    idKabs: Mapped[int] = Column(Integer(), ForeignKey("kabs.id"))
    idDays: Mapped[int] = Column(Integer(), ForeignKey("days.id"))
    tstart: Mapped[str] = Column(String(5), nullable=True)
    tend: Mapped[str] = Column(String(5), nullable=True)
    comment: Mapped[str] = Column(String(100), nullable=True)
    name: Mapped[str] = Column(String(100), nullable=True)

    groups = relationship("Groups", back_populates="rasp")
    kabs = relationship("Kabs", back_populates="rasp")
    days = relationship("Days", back_populates="rasp")
