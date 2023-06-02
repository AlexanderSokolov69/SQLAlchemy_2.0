from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Mapped, relationship
from datetime import date, datetime

from db_base import Base


class Zregister(Base):
    __tablename__ = "zregister"

    headers = {'id': 'ID',
               'year': 'Уч.год',
               'idUsers': 'ID пользователя',
               'idCourses': 'ID курса',
               'sertificate': 'Сертификат',
               'fam': 'Фамилия',
               'ima': 'ИМя',
               'otch': 'Отчество',
               'bithday': 'Д.рожд.',
               'phone': 'Телефон',
               'email': 'е-мейл',
               'zfio': 'ФИО заявителя',
               'comment': 'Доп.информация',
               'checked': 'Тест',
               'regdate': 'Дата',
               'school': 'Уч.заведение',
               'klass': 'Класс',
               'address': 'Адрес',
               'idPlaces': 'ID школы',
               'resume': 'Резюме',
               'letter': 'Письмо',
               'is_ok': 'Принят',
               'smena': 'Уч.смена',
               }

    id: Mapped[int] = Column(Integer(), primary_key=True, autoincrement=True)
    year: Mapped[int] = Column(Integer(), nullable=True)
    idUsers: Mapped[int] = Column(Integer(), ForeignKey("users.id"))
    idCourses: Mapped[int] = Column(Integer(), ForeignKey("courses.id"))
    idPlaces: Mapped[int] = Column(Integer(), ForeignKey("places.id"))
    sertificate: Mapped[str] = Column(String(20), nullable=True)
    fam: Mapped[str] = Column(String(20), nullable=True)
    ima: Mapped[str] = Column(String(20), nullable=True)
    otch: Mapped[str] = Column(String(20), nullable=True)
    birthday: Mapped[str] = Column(String(10), nullable=True)
    phone: Mapped[str] = Column(String(20), nullable=True)
    email: Mapped[str] = Column(String(50), nullable=True)
    zfio: Mapped[str] = Column(String(40), nullable=True)
    comment: Mapped[str] = Column(String(200), nullable=True)
    checked: Mapped[str] = Column(Integer(), nullable=True)
    regdate: Mapped[str] = Column(String(20), nullable=True)
    school: Mapped[str] = Column(String(50), nullable=True)
    klass: Mapped[str] = Column(String(20), nullable=True)
    address: Mapped[str] = Column(String(40), nullable=True)
    resume: Mapped[str] = Column(String(200), nullable=True)
    letter: Mapped[str] = Column(Integer(), nullable=True)
    is_ok: Mapped[str] = Column(Integer(), nullable=True)
    smena: Mapped[str] = Column(Integer(), nullable=True, default=0)

    users = relationship("Users", back_populates="zregister")
    courses = relationship("Courses", back_populates="zregister")
    places = relationship("Places", back_populates="zregister")
