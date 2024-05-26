# -*- coding:utf-8 -*-
# Author: Zachary
from pydantic import BaseModel


class ResultBase:
    code: str
    msg: str
    data: dict


class ResultModel(BaseModel, ResultBase):
    ...


class Result(ResultBase):
    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    @classmethod
    def success(cls, data: object = None, code: str = "200", msg: str = "success"):
        if not data:
            data = {}
        return cls(code, msg, data)

    @classmethod
    def error(cls, data: object = None, code: str = "500", msg: str = "error"):
        if not data:
            data = {}
        return cls(code, msg, data)
