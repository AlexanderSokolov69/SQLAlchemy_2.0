from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date
from .datein import DateIn
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

from .db_base import Base


class Users(Base, UserMixin):
    __tablename__ = "users"

    headers = {'id': 'ID',
               'name': 'Фамилия И.О.:',
               'fam': 'Фамилия:',
               'ima': 'Имя:',
               'otch': 'Отчество:',
               'login': 'Логин для входа в программу:',
               'phone': 'Номер телефона:',
               'email': 'e-mail адрес:',
               'birthday': 'Дата рождения:',
               'idRoles': 'Роль доступа:',
               'idPlaces': 'Место работы/учёбы:',
               'comment': 'Дополнительная информация:',
               'sertificate': 'Сертификат ПФДО:',
               'navigator': 'Публикация в Навигаторе (1/0):',
               'winlogin': 'Имя входа в Windows:',
               'passwd': 'hash-пароля:'
               }
    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(40), nullable=True)
    fam: Mapped[str] = Column(String(40), nullable=True)
    ima: Mapped[str] = Column(String(40), nullable=True)
    otch: Mapped[str] = Column(String(40), nullable=True)
    login: Mapped[str] = Column(String(20), nullable=True)
    phone: Mapped[str] = Column(String(16), nullable=True)
    email: Mapped[str] = Column(String(40), nullable=True)
    birthday: [date] = Column(String(25), nullable=True)
    idRoles: Mapped[int] = Column(Integer)
    idPlaces: Mapped[int] = Column(Integer)
    comment: Mapped[str] = Column(String(200), nullable=True)
    sertificate: Mapped[str] = Column(String(16), nullable=True)
    navigator: Mapped[str] = Column(String(1), nullable=True)
    passwd: Mapped[str] = Column(BLOB(400))
    winlogin: Mapped[str] = Column(String(30), nullable=True)

    groups = relationship("Groups", back_populates="users")
    group_table = relationship("GroupTable", back_populates="users")
    access = relationship("Access", back_populates="users")
    zregister = relationship("Zregister", back_populates="users")

    def set_password(self, password):
        self.passwd = generate_password_hash(password)

    def check_password(self,  password):
        # return check_password_hash(self.passwd, password)
        return True
