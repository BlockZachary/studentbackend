# -*- coding:utf-8 -*-
# Author: Zachary
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from model import Base


class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(255), nullable=False)
    gender: Mapped[str] = mapped_column(String(255), nullable=False)
    birthday: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(255), nullable=False)


class StudentBase(BaseModel):
    username: str
    password: str = Field(..., min_length=1)
    name: Optional[str] = None
    role: Optional[str] = None


class StudentSearch(BaseModel):
    username: str | None
    name: str | None


class StudentCreate(StudentBase):
    phone: Optional[str] = None
    gender: Optional[str] = None
    birthday: Optional[str] = Field(None)
    avatar: Optional[str] = Field(None)


class StudentUpdate(StudentCreate):
    id: int
