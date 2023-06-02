from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date

from db_base import Base


class Journals(Base):
    __tablename__ = "journals"

    headers = {'id': 'ID',
               'idGroups': 'Учебная группа:',
               'Date': 'Дата занятия',
               'tstart': 'Начало занятий:',
               'tend': 'Окончание занятий:',
               'name': 'Тема занятия:',
               'present': 'Отметки о посещении',
               'estim': 'Отметки',
               'shtraf': 'Штрафы',
               'comment': 'Доп. информация',
               'usercomm': 'Комментарии'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    idGroups: Mapped[int] = Column(Integer(), ForeignKey("groups.id"))
    date: Mapped[date] = Column(String(25), nullable=True)
    tstart: Mapped[str] = Column(String(5), nullable=True)
    tend: Mapped[str] = Column(String(5), nullable=True)
    name: Mapped[str] = Column(String(100), nullable=True)
    present: Mapped[str] = Column(String(1500), nullable=True)
    estim: Mapped[str] = Column(String(2000), nullable=True)
    shtraf: Mapped[str] = Column(String(2000), nullable=True)
    comment: Mapped[str] = Column(String(100), nullable=True)
    usercomm: Mapped[str] = Column(String(2048), nullable=True)

    groups = relationship("Groups", back_populates="journals")
