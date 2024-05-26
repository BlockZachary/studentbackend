# -*- coding:utf-8 -*-
# Author: Zachary
from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from model import Base


class Course(Base):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    number: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    periods: Mapped[str] = mapped_column(String(255), nullable=False)
    teacher: Mapped[str] = mapped_column(String(255), nullable=False)


class CourseSearch(BaseModel):
    name: str | None
    number: str | None
    teacher: str | None


class CourseBase(BaseModel):
    name: str
    number: str
    description: str
    periods: str
    teacher: str


class CourseCreate(CourseBase):
    ...


class CourseUpdate(CourseBase):
    id: int
