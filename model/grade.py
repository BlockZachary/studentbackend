# -*- coding:utf-8 -*-
# Author: Zachary
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Integer, String, Double, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import Base
from model.course import Course
from model.student import Student


class Grade(Base):
    __tablename__ = 'grade'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    courseId: Mapped[int] = mapped_column("course_id", Integer, ForeignKey('course.id'), nullable=False)
    studentId: Mapped[int] = mapped_column("student_id", Integer, ForeignKey('student.id'), nullable=False)
    score: Mapped[float] = mapped_column(Double, nullable=False)
    comment: Mapped[str] = mapped_column(String(255), nullable=False)
    feedback: Mapped[str] = mapped_column(String(255), nullable=False)

    student: Mapped[Student] = relationship(lazy=False, backref="grade")
    course: Mapped[Course] = relationship(lazy=False, backref="grade")


class GradeBase(BaseModel):
    courseId: int
    studentId: int
    score: Optional[float] = None
    comment: Optional[str] = None
    feedback: Optional[str] = None


class GradeCreate(GradeBase):
    pass


class GradeSearch(BaseModel):
    courseName: str | None
    studentName: str | None
    studentId: str | None


class GradeUpdate(GradeBase):
    id: int
