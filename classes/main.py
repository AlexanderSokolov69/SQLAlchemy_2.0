import pyodbc
from sqlalchemy import create_engine
from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Session, registry
from sqlalchemy.orm import DeclarativeBase, Mapped
from datetime import date

from datein import DateIn
from db_base import Base
from db_groups import Groups
from db_users import Users
from db_courses import Courses
from db_grouptable import GroupTable
from db_journals import Journals
from db_access import Access
from db_roles import Roles
from db_priv import Priv
from db_days import Days
from db_log import Log
from db_monts import Monts
from db_params import Params
from db_places import Places
from db_rasp import Rasp
from db_kabs import Kabs
from db_times import Times
from db_zregister import Zregister


# engine = create_engine("sqlite+pysqlite:///db/database_J2023_44.db", echo=True, future=True)
engine = create_engine(
    "mssql+pyodbc://sa:Prestige2011!@172.16.1.12:1433/Journal4303?driver=ODBC+Driver+17+for+SQL+Server",
    echo=True, future=True
)

mapper_registry = registry()
Base.metadata.create_all(engine)

if __name__ == "__main__":
    with engine.connect() as conn:
        result = conn.execute(
            Select(GroupTable).join(Users, Users.id == GroupTable.idUsers)
        )
        print(GroupTable.headers)
        for rec in result:

            print(rec)
