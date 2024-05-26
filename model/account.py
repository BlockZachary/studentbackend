# -*- coding:utf-8 -*-
# Author: Zachary
from pydantic import BaseModel


class AccountLogin(BaseModel):
    username: str
    password: str
    role: str


class AccountLoginResponse:
    id: int
    username: str
    name: str
    role: str
    token: str


class AccountRegister(BaseModel):
    username: str
    password: str
