# -*- coding:utf-8 -*-
# Author: Zachary
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from common.constant import *


class Base(DeclarativeBase):
    pass


# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
# echo - True:输出sqlalchemy日志 False:不输出sqlalchemy日志
engine = create_engine(
    f"{MYSQL_DIALECT}://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4",
    echo=True
)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
