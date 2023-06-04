from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from .db_base import Base


class Priv(Base):
    __tablename__ = "priv"

    headers = {'id': 'ID',
               'name': 'Привелегия:',
               'access': 'Доступ',
               'comment': 'Комментарий:'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(40), nullable=True)
    access: Mapped[str] = Column(String(10), nullable=True)
    comment: Mapped[str] = Column(String(100), nullable=True)

    roles = relationship("Roles", back_populates="priv")
