import pyodbc
import sqlalchemy as sa
from sqlalchemy import text, MetaData, Table, Select
from sqlalchemy.orm import Session, registry, declarative_base

if __name__ == '__main__':
    sa_version = sa.__version__.split('.')
    print(sa_version)
    engine = sa.create_engine("sqlite+pysqlite:///db/database_J2023.db", echo=False, future=True)
    # engine = sa.create_engine(
    #     "mssql+pyodbc://sa:Prestige2011!@172.16.1.12:1433/Journal4303?driver=ODBC+Driver+17+for+SQL+Server",
    #     echo=True, future=True
    # )

    metadata_obj = MetaData()
    metadata_obj.reflect(bind=engine)

    users = metadata_obj.tables['users']
    groups = metadata_obj.tables['groups']

    with Session(engine) as session:
        result = session.execute(
            Select(users.c.id, users.c.name, groups.c.name).
            join(groups, groups.c.idUsers == users.c.id).
            where(users.c.id == 15)
        )
        print(result.all())
