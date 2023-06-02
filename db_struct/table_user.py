from db_session import *


class Users(Base):
    __tablename__ = "users"

    id: [int] = Column(Integer, primary_key=True, autoincrement=True)
    name: [str] = Column(String(30), nullable=True)
