# -*- coding:utf-8 -*-
# Author: Zachary
from enum import Enum


class Role(str, Enum):
    ADMIN = "管理员"
    STUDENT = "学生"
