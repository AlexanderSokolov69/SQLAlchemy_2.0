import sqlalchemy as sa
from sqlalchemy import text, MetaData
from sqlalchemy.orm import Session


if __name__ == '__main__':
    sa_version = sa.__version__.split('.')
    print(sa_version)
    engine = sa.create_engine("sqlite+pysqlite:///db/database.db", echo=True, future=True)
#    engine = sa.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

    with engine.connect() as conn:
        # conn.execute(text("CREATE TABLE some_table (x int, y int)"))
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
        )
        conn.commit()

    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
        )

    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
        )
        conn.commit()

    with engine.connect() as conn:
        result = conn.execute(text("SELECT x, y FROM some_table"))
        for row in result:
            print(f"x: {row.x:2}  y: {row.y:2}")

    with engine.connect() as conn:
        result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :dy"), {"dy": 2})
        for row in result:
            print(f"x: {row.x:2}  y: {row.y:2}")

    stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
    with Session(engine) as session:
        result = session.execute(stmt, {"y": 6})
        for row in result:
            print(f"x: {row.x}  y: {row.y}")
