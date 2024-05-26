# -*- coding:utf-8 -*-
# Author: Zachary

# 用于更新对象属性
def set_attrs(obj, data: dict):
    if data:
        for key, value in data.items():
            setattr(obj, key, value)
