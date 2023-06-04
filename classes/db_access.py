from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from .db_base import Base


class Access(Base):
    __tablename__ = "access"

    headers = {'id': 'ID',
               'idUser': 'Пользователь:',
               'datetime': 'Дата доступа',
               'sel': 'Начало занятий:',
               'idRole': 'ID роли:'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    idUser: Mapped[int] = Column(ForeignKey("users.id"))
    datetime: Mapped[datetime] = Column(String(300), nullable=True)
    idRole: Mapped[int] = Column(ForeignKey("roles.id"))

    users = relationship("Users", back_populates="access")
    roles = relationship("Roles", back_populates="access")
