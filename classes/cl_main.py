import pyodbc
from datetime import date
# SQLAlchemy import
from sqlalchemy import create_engine
from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Session, registry, sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy import select
# Flask import
from flask import flash

from .datein import DateIn

from .db_base import Base
from .db_groups import Groups
from .db_users import Users
from .db_courses import Courses
from .db_grouptable import GroupTable
from .db_journals import Journals
from .db_access import Access
from .db_roles import Roles
from .db_priv import Priv
from .db_days import Days
from .db_log import Log
from .db_monts import Monts
from .db_params import Params
from .db_places import Places
from .db_rasp import Rasp
from .db_kabs import Kabs
from .db_times import Times
from .db_zregister import Zregister

__factory = None


def init_db(connect_string: str, echo=True):
    global __factory
    if __factory is None:
        try:
            engine = create_engine(connect_string, echo=echo, future=True)
            Base.metadata.create_all(engine)
            #     mapper_registry = registry()
            __factory = sessionmaker(bind=engine)
        except Exception as err:
            flash(f"Ошибка подключения SQL: {err}", category='error')
            __factory = None

        # 1 engine = create_engine("sqlite+pysqlite:///db/database_J2023.db", echo=True, future=True)
        # 2 engine = create_engine(
        # 2     "mssql+pyodbc://sa:Prestige2011!@172.16.1.12:1433/Journal4303?driver=ODBC+Driver+17+for+SQL+Server",
        # 2     echo=True, future=True
        # 2 )
    try:
        return __factory()
    except Exception as err:
        flash(f"Ошибка создания сессии: {err}", category='error')


if __name__ == "__main__":
    pass
    with init_db("sqlite+pysqlite:///db/database_J2023.db").connect() as conn:
        result = conn.execute(
            Select(GroupTable, Users).join(Users, Users.id == GroupTable.idUsers)
        )
        print(GroupTable.headers)
        for rec in result:

            print(rec)

    # stmt = select(Groups.id, Groups.name, Users.name, Courses.name).\
    #     join(Courses).\
    #     join(Users).where(Courses.year == 2023)
    # print(stmt)
    #
    # with Session(engine) as session:
    #     for row in session.execute(stmt):
    #         print(row)
    #

