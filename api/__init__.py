# -*- coding:utf-8 -*-
# Author: Zachary
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# 跨域问题
origins = ["http://localhost:5173", "http://127.0.0.1:5173"]  # 替换为你的前端应用的实际地址

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许跨域访问的来源域名列表
    allow_credentials=True,  # 是否允许携带cookie
    allow_methods=["*"],  # 允许的方法，默认包含常见的GET、POST等，"*"表示所有方法
    allow_headers=["*"],  # 允许的请求头，默认包含常见的Content-Type等，"*"表示所有请求头
)

from api import adminApi, exceptionHandler, courseApi, studentApi, fileApi, studentCourseApi, gradeApi
