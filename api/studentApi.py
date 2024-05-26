# -*- coding:utf-8 -*-
# Author: Zachary
from typing import Optional

from fastapi import Depends, APIRouter, Query

from api import app
from common.auth import auth_handler
from common.pageHelper import PageHelper
from common.result import ResultModel, Result
from model import Session, get_db_session
from model.account import AccountRegister
from model.student import StudentSearch, StudentCreate, StudentUpdate
from service.studentService import StudentService


@app.post("/register", response_model=ResultModel)
async def register(account: AccountRegister, db_session: Session = Depends(get_db_session)):
    StudentService.register(account, db_session)
    return Result.success()


student_router = APIRouter(prefix="/student", dependencies=[Depends(auth_handler.auth_required)])


@student_router.get("/selectPage", response_model=ResultModel)
async def select_page(page: int = Query(1, ge=1, alias="pageNum", description="Page number"),
                      size: int = Query(5, gt=0, le=100, alias="pageSize", description="Page size"),
                      username: Optional[str] = Query(None, description="Student username"),
                      name: Optional[str] = Query(None, description="Student name"),
                      db_session: Session = Depends(get_db_session)):
    pageInfo = PageHelper.startPage(page, size)
    student_search = StudentSearch(username=username, name=name)
    student_list = StudentService.select_page(student_search, db_session)
    return Result.success(pageInfo.of(student_list))


@student_router.post("/add", response_model=ResultModel)
async def add(student: StudentCreate, db_session: Session = Depends(get_db_session)):
    StudentService.add_student(student, db_session)
    return Result.success()


@student_router.put("/update", response_model=ResultModel)
async def update(student: StudentUpdate, db_session: Session = Depends(get_db_session)):
    StudentService.update_by_id(student, db_session)
    return Result.success()


@student_router.delete("/delete/{id}", response_model=ResultModel)
async def delete(id: int, db_session: Session = Depends(get_db_session)):
    StudentService.delete_by_id(id, db_session)
    return Result.success()


app.include_router(student_router)
