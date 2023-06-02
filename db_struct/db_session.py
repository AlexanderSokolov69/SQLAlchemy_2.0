import pyodbc
import sqlalchemy as sa
from sqlalchemy import text, MetaData, Table, Column, Select, Integer, String, ForeignKey, BLOB, Boolean
from sqlalchemy import Date, insert
from sqlalchemy.orm import Session, registry
from sqlalchemy.orm import declarative_base
from datetime import date

sa_version = sa.__version__.split('.')
print(sa_version)

engine = sa.create_engine("sqlite+pysqlite:///db/database_J2023_1.db", echo=True, future=True)
# engine = sa.create_engine(
#     "mssql+pyodbc://sa:Prestige2011!@172.16.1.12:1433/Journal4303?driver=ODBC+Driver+17+for+SQL+Server",
#     echo=True, future=True
# )

Base = declarative_base()
mapper_registry = registry()


class Users(Base):
    __tablename__ = "users"

    id: [int] = Column(Integer, primary_key=True, autoincrement=True)
    name: [str] = Column(String(30), nullable=True)


mapper_registry.metadata.create_all(engine)