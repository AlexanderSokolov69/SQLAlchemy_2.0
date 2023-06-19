from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    headers = {}
    def __repr__(self):
        return f"{self.__tablename__} | {self.id}  | {self.headers}"
