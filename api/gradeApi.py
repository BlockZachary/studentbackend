# -*- coding:utf-8 -*-
# Author: Zachary
from typing import Optional

from fastapi import APIRouter, Depends, Query

from api import app
from common.pageHelper import PageHelper
from common.result import ResultModel, Result
from model import Session, get_db_session
from model.grade import GradeCreate, GradeSearch, GradeUpdate
from service.gradeService import GradeService

grade_router = APIRouter(prefix='/grade')


@grade_router.post('/add', response_model=ResultModel)
async def add(grade: GradeCreate, db_session: Session = Depends(get_db_session)):
    GradeService.add_grade(grade, db_session)
    return Result.success()


@grade_router.get("/selectPage", response_model=ResultModel)
async def select_page(page: int = Query(1, ge=1, alias="pageNum", description="Page number"),
                      size: int = Query(5, gt=0, le=100, alias="pageSize", description="Page size"),
                      studentName: Optional[str] = Query(None, description="Student name"),
                      courseName: Optional[str] = Query(None, description="Course name"),
                      studentId: Optional[str] = Query(None, description="Student id"),
                      db_session: Session = Depends(get_db_session)):
    pageInfo = PageHelper.startPage(page, size)
    grade_search: GradeSearch = GradeSearch(studentName=studentName, courseName=courseName, studentId=studentId)
    grade_list = GradeService.select_page(grade_search, db_session)
    return Result.success(pageInfo.of(grade_list))


@grade_router.put("/update", response_model=ResultModel)
async def update(grade: GradeUpdate, db_session: Session = Depends(get_db_session)):
    GradeService.update_by_id(grade, db_session)
    return Result.success()


@grade_router.delete("/delete/{id}", response_model=ResultModel)
async def delete(id: int, db_session: Session = Depends(get_db_session)):
    GradeService.delete_by_id(id, db_session)
    return Result.success()


app.include_router(grade_router)
