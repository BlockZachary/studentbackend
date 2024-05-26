# -*- coding:utf-8 -*-
# Author: Zachary
from common.config import config

HOST = config.env.get("HOST")
PORT = config.env.get("PORT")

MYSQL_DIALECT = config.env.get("MYSQL_DIALECT")
MYSQL_HOST = config.env.get("MYSQL_HOST")
MYSQL_PORT = config.env.get("MYSQL_PORT")
MYSQL_USER = config.env.get("MYSQL_USER")
MYSQL_PASSWORD = config.env.get("MYSQL_PASSWORD")
MYSQL_DATABASE = config.env.get("MYSQL_DATABASE")

TOKEN_EXPIRE_DAYS = 7
TOKEN_EXPIRE_MINUTES = 0
TOKEN_EXPIRE_SECONDS = 0