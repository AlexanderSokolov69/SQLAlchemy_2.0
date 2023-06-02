from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date

from db_base import Base


class Courses(Base):
    __tablename__ = "courses"

    headers = {'id': 'ID',
               'name': 'Наименование учебного курса:',
               'volume': 'Объём курса в акк.часах:',
               'lesson': 'Занятий в нед.:',
               'target': 'Возрастная группа:',
               'acchour': 'Академ.час:',
               'hday': 'Занятий в день:',
               'url': 'Ссылка на раздел на сайте:',
               'year': 'Учебный год:',
               'comment': 'Доп.информация',
               'c_open': 'Активен'
               }
    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(100), nullable=True)
    volume: Mapped[int] = Column(Integer)
    lesson: Mapped[int] = Column(Integer)
    url: Mapped[str] = Column(String(200), nullable=True)
    year: Mapped[int] = Column(Integer)
    target: Mapped[str] = Column(String(20), nullable=True)
    comment: Mapped[str] = Column(String(100), nullable=True)
    acchour: Mapped[int] = Column(Integer)
    hday: Mapped[int] = Column(Integer)
    c_open: Mapped[int] = Column(Integer)

    zregister = relationship("Zregister", back_populates="courses")
