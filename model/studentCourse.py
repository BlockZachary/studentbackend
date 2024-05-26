# -*- coding:utf-8 -*-
# Author: Zachary
from pydantic import BaseModel
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import Base
from model.student import Student


class StudentCourse(Base):
    __tablename__ = "student_course"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    number: Mapped[str] = mapped_column(String(255), nullable=False)
    studentId: Mapped[int] = mapped_column("student_id", Integer, ForeignKey('student.id'), nullable=False)
    courseId: Mapped[int] = mapped_column("course_id", Integer, nullable=False)

    student: Mapped[Student] = relationship(lazy=False, backref="student_course")


class StudentCourseBase(BaseModel):
    name: str
    number: str
    studentId: int
    courseId: int


class StudentCourseCreate(StudentCourseBase):
    pass


class StudentCourseSearch(BaseModel):
    name: str | None
    number: str | None
    studentId: str | None
