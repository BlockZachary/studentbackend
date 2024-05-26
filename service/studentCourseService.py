# -*- coding:utf-8 -*-
# Author: Zachary
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, and_, asc

from common.utils import set_attrs
from exception.customException import StudentCourseExistException, StudentCourseNotExistException
from model import Session
from model.student import Student
from model.studentCourse import StudentCourseCreate, StudentCourse, StudentCourseSearch


class StudentCourseService:

    @staticmethod
    def add_student_course(student_course: StudentCourseCreate, db_session: Session):
        query = select(StudentCourse).where(
            and_(StudentCourse.studentId == student_course.studentId,
                 StudentCourse.courseId == student_course.courseId))
        exist_student_course: StudentCourse = db_session.execute(query).scalar()
        if exist_student_course:
            raise StudentCourseExistException("课程已选过")
        new_student_course = StudentCourse()
        set_attrs(new_student_course, jsonable_encoder(student_course))
        db_session.add(new_student_course)
        db_session.commit()
        return new_student_course

    @staticmethod
    def select_page(student_course_search: StudentCourseSearch, db_session: Session):
        query = select(StudentCourse, Student).join(StudentCourse.student).order_by(asc(StudentCourse.id))
        if student_course_search.name:
            query = query.where(StudentCourse.name.like(f"%{student_course_search.name}%"))
        if student_course_search.number:
            query = query.where(StudentCourse.number.like(f"%{student_course_search.number}%"))
        if student_course_search.studentId:
            query = query.where(StudentCourse.studentId == student_course_search.studentId)
        result = db_session.execute(query).scalars().all()
        return result

    @staticmethod
    def delete_by_id(id: int, db_session: Session):
        exist_student_course: StudentCourse = check_student_course_exist(id, db_session)
        db_session.delete(exist_student_course)
        db_session.commit()
        return exist_student_course


def check_student_course_exist(student_course_id: int, db_session: Session):
    query = select(StudentCourse).where(StudentCourse.id == student_course_id)
    exist_student_course: StudentCourse = db_session.execute(query).scalar()
    if not exist_student_course:
        raise StudentCourseNotExistException("选课记录不存在")
    return exist_student_course
