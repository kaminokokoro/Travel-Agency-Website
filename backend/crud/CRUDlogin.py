from typing import Any

from backend.crud.CRUDbase import crud_base
from backend.db.db import session_scope
from backend.db.model import User
from backend.util import passutil



class CRUDLogin:

    def check_username_password(self,phone_number:str, password: str) -> Any:
        """ Verify Password"""
        password_hash = crud_base.get_user_password(phone_number)
        # return password_hash==password
        return passutil.verify_password(password, password_hash)

    def get_user_login(self, phone_number: str) -> Any:
        """ Get User"""
        with session_scope() as db:
            user = db.query(User).filter(User.phone_number == phone_number).first()
            return user







    # def login_user(self,phone_number:str):
    #     with session_scope() as db:
    #         # print("find user")
    #         user = db.query(User).filter(User.phone_number == phone_number).first()
    #         # print("login")
    #         # print(user.__repr__())
    #         if user is None:
    #             return None
    #         db.commit()
    #         db.refresh(user)
    #         return None





crud_login = CRUDLogin()

