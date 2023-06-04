from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date

from .db_base import Base


class GroupTable(Base):
    __tablename__ = "group_table"

    headers = {'id': 'ID',
               'idGroups': 'Учебная группа:',
               'idUsers': 'Фамилия И.О. кубиста:',
               'best': 'Сертификат',
               'comment': 'Доп. информация'
               }
    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    idGroups: Mapped[int] = Column(ForeignKey("groups.id"))
    idUsers: Mapped[int] = Column(ForeignKey("users.id"))
    comment: Mapped[str] = Column(String(200), nullable=True)
    best: Mapped[str] = Column(String(16), nullable=True)

    users = relationship("Users", back_populates="group_table")
    groups = relationship("Groups", back_populates="group_table")
