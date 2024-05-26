# -*- coding:utf-8 -*-
# Author: Zachary

class UserNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message


class UserExistException(Exception):
    def __init__(self, message: str):
        self.message = message


class PasswordNotMatchException(Exception):
    def __init__(self, message: str):
        self.message = message


class TokenException(Exception):
    def __init__(self, message: str):
        self.message = message


class CourseExistException(Exception):
    def __init__(self, message: str):
        self.message = message


class CourseNotExistException(Exception):
    def __init__(self, message: str):
        self.message = message


class FileNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message


class StudentCourseExistException(Exception):
    def __init__(self, message: str):
        self.message = message


class StudentCourseNotExistException(Exception):
    def __init__(self, message: str):
        self.message = message


class GradeExistException(Exception):
    def __init__(self, message: str):
        self.message = message
