# -*- coding:utf-8 -*-
# Author: Zachary
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select

from common.auth import auth_handler
from common.utils import set_attrs
from exception.customException import UserNotFoundException, PasswordNotMatchException
from model import Session
from model.account import AccountLogin, AccountLoginResponse
from model.admin import AdminModel, Admin, AdminLoginResponse


class AdminService:

    @staticmethod
    def login(account: AccountLogin, db_session: Session) -> AccountLoginResponse:
        query = select(Admin).where(Admin.username == account.username)
        exist_admin: Admin = db_session.execute(query).scalars().first()
        if not exist_admin:
            raise UserNotFoundException("用户不存在")
        if not auth_handler.verify_password(account.password, exist_admin.password):
            raise PasswordNotMatchException("身份验证未通过")
        account_login_response = AccountLoginResponse()
        set_attrs(account_login_response, jsonable_encoder(exist_admin))
        account_login_response.token = auth_handler.encode_token(exist_admin.id)
        return account_login_response
