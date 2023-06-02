from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date

from db_base import Base


class Groups(Base):
    __tablename__ = "groups"

    headers = {'id': 'ID',
               'name': 'Кодовое название учебной группы',
               'idCourses': 'ID Учебной программы',
               'idUsers': 'Фамилия И.О. наставника',
               'comment': 'Доп. информация'
               }
    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(40), nullable=True)
    idCourses: Mapped[int] = Column(Integer(), ForeignKey("courses.id"))
    idUsers: Mapped[int] = Column(Integer(), ForeignKey("users.id"))
    comment: Mapped[str] = Column(String(200), nullable=True)

    users = relationship("Users", back_populates="groups")
    group_table = relationship("GroupTable", back_populates="groups")
    journals = relationship("Journals", back_populates="groups")
    rasp = relationship("Rasp", back_populates="groups")