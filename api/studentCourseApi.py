# -*- coding:utf-8 -*-
# Author: Zachary
from typing import Optional

from fastapi import APIRouter, Depends, Query

from api import app
from common.pageHelper import PageHelper
from common.result import ResultModel, Result
from model import Session, get_db_session
from model.studentCourse import StudentCourseCreate, StudentCourseSearch
from service.studentCourseService import StudentCourseService

student_course_router = APIRouter(prefix="/studentCourse")


@student_course_router.post("/add", response_model=ResultModel)
async def add(student_course: StudentCourseCreate, db_session: Session = Depends(get_db_session)):
    StudentCourseService.add_student_course(student_course, db_session)
    return Result.success()


@student_course_router.get("/selectPage", response_model=ResultModel)
async def select_page(page: int = Query(1, ge=1, alias="pageNum", description="Page number"),
                      size: int = Query(5, gt=0, le=100, alias="pageSize", description="Page size"),
                      name: Optional[str] = Query(None, description="Course name"),
                      number: Optional[str] = Query(None, description="Course number"),
                      studentId: Optional[str] = Query(None, description="Student id"),
                      db_session: Session = Depends(get_db_session)):
    pageInfo = PageHelper.startPage(page, size)
    student_course_search = StudentCourseSearch(name=name, number=number, studentId=studentId)
    student_list = StudentCourseService.select_page(student_course_search, db_session)
    return Result.success(pageInfo.of(student_list))


@student_course_router.delete("/delete/{id}", response_model=ResultModel)
async def delete(id: int, db_session: Session = Depends(get_db_session)):
    StudentCourseService.delete_by_id(id, db_session)
    return Result.success()


app.include_router(student_course_router)
