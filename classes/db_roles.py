from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from db_base import Base


class Roles(Base):
    __tablename__ = "roles"

    headers = {'id': 'ID',
               'idPriv': 'ID Прив.',
               'name': 'Роль доступа',
               'comment': 'Комментарий:'
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    idPriv: Mapped[int] = Column(Integer(), ForeignKey("priv.id"))
    name: Mapped[str] = Column(String(200), nullable=True)
    comment: Mapped[str] = Column(String(100), nullable=True)

    priv = relationship("Priv", back_populates="roles")
    access = relationship("Access", back_populates="roles")
