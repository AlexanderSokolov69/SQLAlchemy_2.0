import pyodbc
import sqlalchemy as sa
from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date
from sqlalchemy.orm import Session, registry
from sqlalchemy.orm import declarative_base
from datetime import date

from metods.datein import DateIn

if __name__ == '__main__':
    sa_version = sa.__version__.split('.')
    print(sa_version)
    engine = sa.create_engine("sqlite+pysqlite:///db/database_J2023_1.db", echo=True, future=True)
    # engine = sa.create_engine(
    #     "mssql+pyodbc://sa:Prestige2011!@172.16.1.12:1433/Journal4303?driver=ODBC+Driver+17+for+SQL+Server",
    #     echo=True, future=True
    # )

    # Отражение реальной базы в объект metadata_obj
    # metadata_obj = MetaData()
    # metadata_obj.reflect(bind=engine)
    #
    # users = metadata_obj.tables['users']
    # groups = metadata_obj.tables['groups']
    #

    # with Session(engine) as session:
    #     result = session.execute(
    #         Select(users.c.id, users.c.name, groups.c.name).
    #         join(groups, groups.c.idUsers == users.c.id).
    #         where(users.c.id == 15)
    #     )
    #     print(result.all())

    Base = declarative_base()


    class Users(Base):
        __tablename__ = "users"

        id: [int] = Column(Integer, primary_key=True, autoincrement=True)
        fam: [str] = Column(String(30), nullable=True)
        ima: [str] = Column(String(30), nullable=True)
        otch: [str] = Column(String(30), nullable=True)
        phone: [str] = Column(String(12), nullable=True)
        email: [str] = Column(String(30), nullable=True)
        birthday: [DateIn] = Column(Date, nullable=True)
        comment: [str] = Column(String(200), nullable=True)
        name: [str] = Column(String(30), nullable=True)
        passwd: [str] = Column(BLOB(200), nullable=True)
        login: [str] = Column(String(30), nullable=True)
        sertificate: [str] = Column(String(10), nullable=True)
        navigator: [bool] = Column(Boolean, nullable=True)
        winlogin: [str] = Column(String(20), nullable=True)
        # idRoles = Column(ForeignKey(Roles.id))
        # idPlaces = Column(ForeignKey(Places.id))
        # places = relationship(Places)
        # roles = relationship(Roles)

    Base.metadata.create_all(engine)

    d1 = date.today()
    