# -*- coding:utf-8 -*-
# Author: Zachary
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from api import app
from common.result import Result
from exception.customException import UserNotFoundException, PasswordNotMatchException, TokenException, \
    CourseExistException, CourseNotExistException, UserExistException, FileNotFoundException, \
    StudentCourseExistException, StudentCourseNotExistException, GradeExistException
from fastapi import Request


@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    result = Result.error(code='404', msg=exc.message)
    return JSONResponse(status_code=404, content=jsonable_encoder(result))


@app.exception_handler(PasswordNotMatchException)
async def password_not_match_exception_handler(request: Request, exc: PasswordNotMatchException):
    result = Result.error(code='401', msg=exc.message)
    return JSONResponse(status_code=401, content=jsonable_encoder(result))


@app.exception_handler(TokenException)
async def token_exception_handler(request: Request, exc: TokenException):
    result = Result.error(code='401', msg=exc.message)
    return JSONResponse(status_code=401, content=jsonable_encoder(result))


@app.exception_handler(CourseExistException)
async def course_exist_exception_handler(request: Request, exc: CourseExistException):
    result = Result.error(code='400', msg=exc.message)
    return JSONResponse(status_code=400, content=jsonable_encoder(result))


@app.exception_handler(CourseNotExistException)
async def course_not_exist_exception_handler(request: Request, exc: CourseNotExistException):
    result = Result.error(code='404', msg=exc.message)
    return JSONResponse(status_code=404, content=jsonable_encoder(result))


@app.exception_handler(UserExistException)
async def user_exist_exception_handler(request: Request, exc: UserExistException):
    result = Result.error(code='400', msg=exc.message)
    return JSONResponse(status_code=400, content=jsonable_encoder(result))


@app.exception_handler(FileNotFoundException)
async def file_not_found_exception_handler(request: Request, exc: FileNotFoundException):
    result = Result.error(code='404', msg=exc.message)
    return JSONResponse(status_code=404, content=jsonable_encoder(result))


@app.exception_handler(StudentCourseExistException)
async def student_course_exist_exception_handler(request: Request, exc: StudentCourseExistException):
    result = Result.error(code='400', msg=exc.message)
    return JSONResponse(status_code=400, content=jsonable_encoder(result))


@app.exception_handler(StudentCourseNotExistException)
async def student_course_not_exist_exception_handler(request: Request, exc: StudentCourseNotExistException):
    result = Result.error(code='404', msg=exc.message)
    return JSONResponse(status_code=404, content=jsonable_encoder(result))


@app.exception_handler(GradeExistException)
async def grade_exist_exception_handler(request: Request, exc: GradeExistException):
    result = Result.error(code='400', msg=exc.message)
    return JSONResponse(status_code=400, content=jsonable_encoder(result))
