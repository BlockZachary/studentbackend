# -*- coding:utf-8 -*-
# Author: Zachary
from fastapi.encoders import jsonable_encoder


class Page:
    list: list
    total: int
    pageNum: int
    pageSize: int

    def __init__(self, list, total, pageNum, pageSize):
        self.list = list
        self.total = total
        self.pageNum = pageNum
        self.pageSize = pageSize


class PageHelper:
    page: int
    size: int
    limit: int
    offset: int

    def __init__(self, page: int, size: int, limit: int, offset: int):
        self.page = page
        self.size = size
        self.limit = limit
        self.offset = offset

    @classmethod
    def startPage(cls, page: int, size: int):
        limit = size
        offset = size * (page - 1)
        return cls(page, size, limit, offset)

    def of(self, data):
        data_list = [jsonable_encoder(dataitem) for dataitem in data[self.offset:self.offset + self.limit]]
        data_total = len(data)
        page = Page(data_list, data_total, self.page, self.size)
        return jsonable_encoder(page)
