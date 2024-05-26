# -*- coding:utf-8 -*-
# Author: Zachary
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, asc

from common.Enum import Role
from common.auth import auth_handler
from common.utils import set_attrs
from exception.customException import UserNotFoundException, PasswordNotMatchException, UserExistException
from model import Session
from model.account import AccountLogin, AccountLoginResponse, AccountRegister
from model.student import Student, StudentSearch, StudentCreate, StudentUpdate


class StudentService:
    @staticmethod
    def login(account: AccountLogin, db_session: Session) -> AccountLoginResponse:
        query = select(Student).where(Student.username == account.username)
        exist_student: Student = db_session.execute(query).scalars().first()
        if not exist_student:
            raise UserNotFoundException("用户不存在")
        if not auth_handler.verify_password(account.password, exist_student.password):
            raise PasswordNotMatchException("身份验证未通过")
        account_login_response = AccountLoginResponse()
        set_attrs(account_login_response, jsonable_encoder(exist_student))
        account_login_response.token = auth_handler.encode_token(exist_student.id)
        return account_login_response

    @staticmethod
    def register(account: AccountRegister, db_session: Session) -> Student:
        query = select(Student).where(Student.username == account.username)
        exist_student: Student = db_session.execute(query).scalars().first()
        if exist_student:
            raise UserExistException("账号已存在")

        new_student = Student()
        account.password = auth_handler.get_password_hash(account.password)
        set_attrs(new_student, jsonable_encoder(account))
        if new_student.name is None:
            new_student.name = account.username
        new_student.role = Role.STUDENT.name

        db_session.add(new_student)
        db_session.commit()
        return new_student

    @staticmethod
    def select_page(student_search: StudentSearch, db_session: Session):
        query = select(Student).order_by(asc(Student.id))
        if student_search.username:
            query = query.where(Student.username.like(f"%{student_search.username}%"))
        if student_search.name:
            query = query.where(Student.name.like(f"%{student_search.name}%"))

        result = db_session.execute(query).scalars().all()
        return result

    @staticmethod
    def add_student(student: StudentCreate, db_session: Session):
        query = select(Student).where(Student.username == student.username)
        exist_student: Student = db_session.execute(query).scalars().all()
        if exist_student:
            raise UserExistException("账号已存在")

        student.password = auth_handler.get_password_hash(student.password)
        student = Student(**student.dict())
        if student.name is None:
            student.name = student.username
        student.role = Role.STUDENT.name
        db_session.add(student)
        db_session.commit()
        return student

    @staticmethod
    def update_by_id(student: StudentUpdate, db_session: Session):
        exist_student: Student = check_student_exist(student.id, db_session)
        student.password = auth_handler.get_password_hash(student.password)
        set_attrs(exist_student, jsonable_encoder(student))
        db_session.commit()
        return exist_student

    @staticmethod
    def delete_by_id(id: int, db_session: Session):
        exist_student: Student = check_student_exist(id, db_session)
        db_session.delete(exist_student)
        db_session.commit()
        return exist_student


def check_student_exist(student_id: int, db_session: Session):
    query = select(Student).where(Student.id == student_id)
    exist_student: Student = db_session.execute(query).scalar()
    if not exist_student:
        raise UserNotFoundException("账号不存在")
    return exist_student
