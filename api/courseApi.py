# -*- coding:utf-8 -*-
# Author: Zachary
from typing import Optional

from fastapi import APIRouter, Depends, Query

from api import app
from common.auth import auth_handler
from common.pageHelper import PageHelper
from common.result import ResultModel, Result
from model import Session, get_db_session
from model.course import CourseSearch, CourseCreate, CourseUpdate
from service.courseService import CourseService

course_router = APIRouter(prefix='/course', dependencies=[Depends(auth_handler.auth_required)])


@course_router.get("/selectPage", response_model=ResultModel)
async def select_page(page: int = Query(1, ge=1, alias="pageNum", description="Page number"),
                      size: int = Query(5, gt=0, le=100, alias="pageSize", description="Page size"),
                      name: Optional[str] = Query(None, description="Course name"),
                      number: Optional[str] = Query(None, description="Course number"),
                      teacher: Optional[str] = Query(None, description="Course teacher"),
                      db_session: Session = Depends(get_db_session)):
    pageInfo = PageHelper.startPage(page, size)
    course_search = CourseSearch(name=name, number=number, teacher=teacher)
    course_list = CourseService.select_page(course_search, db_session)
    result = Result.success(pageInfo.of(course_list))
    return result


@course_router.post("/add", response_model=ResultModel)
async def add(course: CourseCreate, db_session: Session = Depends(get_db_session)):
    CourseService.add_course(course, db_session)
    result = Result.success()
    return result


@course_router.put("/update", response_model=ResultModel)
async def update(course: CourseUpdate, db_session: Session = Depends(get_db_session)):
    CourseService.update_by_id(course, db_session)
    result = Result.success()
    return result


@course_router.delete("/delete/{id}", response_model=ResultModel)
async def delete(id: int, db_session: Session = Depends(get_db_session)):
    CourseService.delete_by_id(id, db_session)
    result = Result.success()
    return result


app.include_router(course_router)
