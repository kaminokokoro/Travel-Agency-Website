from fastapi import APIRouter, Depends, HTTPException
from fastapi import Body
from typing import Annotated
from starlette import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import timedelta
from sqlalchemy.orm import Session
from jwt import exceptions
# from jwt.utils import get_int_from_datetime
from datetime import datetime
import uuid
from fastapi.security import OAuth2PasswordRequestForm

from backend.auth.token import access_token
from backend.config import ProjectSettings

from backend.crud.CRUDlogin import crud_login
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user
from backend.util.response_schemas import base_responses, user_response

router_login = APIRouter()


@router_login.post("/getToken", responses=response_schemas.get_token_response)
def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends()) -> JSONResponse:
    """ Return Access Token"""
    db_user = crud_login.get_user_login(phone_number=form_data.username)
    if db_user is None:
        return JSONResponse(status_code=400,
                            content={"message": "Invalid Credentials"})
    else:
        is_password_correct = crud_login.check_username_password(
            phone_number=form_data.username,
            password=form_data.password)
        if is_password_correct is False:
            return JSONResponse(status_code=400,
                                content={"message": "Invalid Credentials"})
        else:
            access_token_expires = timedelta(
                minutes=ProjectSettings.ACCESS_TOKEN_EXPIRE_MINUTES)
            token = access_token.create_access_token(
                data={"sub": db_user.id},
                expires_delta=access_token_expires)
            return JSONResponse(status_code=200,
                                content={"access_token": token,
                                         "token_type": "Bearer",
                                         })


@router_login.post("/login",
                   responses=response_schemas.login_response)
def login_user(user: Annotated[
    schemas.UserLogIn,
    Body(openapi_examples={
        "login": {
            "summary": "Login",
            "description": "Login User",
            "value": {
                "phone_number": "123",
                "password": "123"
            }}})]
               ) -> JSONResponse:
    """ Login user and Return Access Token"""

    # print(user.phone_number,user.password)
    db_user = crud_login.get_user_login(phone_number=user.phone_number)
    # print(db_user)
    if db_user is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    else:
        is_password_correct = crud_login.check_username_password(
            phone_number=user.phone_number,
            password=user.password)
        if is_password_correct is False:
            return JSONResponse(status_code=400,
                                content={"detail": "Bad Request"})
        else:
            # print("router_login login")
            # crud_login.login_user(phone_number=user.phone_number)
            # print("create token")
            access_token_expires = timedelta(
                minutes=ProjectSettings.ACCESS_TOKEN_EXPIRE_MINUTES)
            token = access_token.create_access_token(
                data={"sub": db_user.id},
                expires_delta=access_token_expires)
            return JSONResponse(status_code=200,
                                content={"access_token": token,
                                         "token_type": "Bearer",
                                         "user_id": jsonable_encoder(db_user.id),
                                         "phone_number": jsonable_encoder(user.phone_number),
                                         "authorization": jsonable_encoder(db_user.authorization)})


# @router_login.post("/login",
#              responses=response_schemas.login_response)
# def login_user(form_data: OAuth2PasswordRequestForm = Depends()) -> JSONResponse:
#     """ Login user and Return Access Token"""
#
#     # print(user.phone_number,user.password)
#     db_user = crud_login.get_user_login(phone_number=form_data.phone_number)
#     # print(db_user)
#     if db_user is None:
#         return JSONResponse(status_code=400,
#                             content={"detail": "Bad Request"})
#     else:
#         is_password_correct = crud_login.check_username_password(
#             phone_number=form_data.phone_number,
#             password=form_data.password)
#         if is_password_correct is False:
#             return JSONResponse(status_code=400,
#                                 content={"detail": "Bad Request"})
#         else:
#             # print("router_login login")
#             # crud_login.login_user(phone_number=user.phone_number)
#             # print("create token")
#             access_token_expires = timedelta(
#                 minutes=ProjectSettings.ACCESS_TOKEN_EXPIRE_MINUTES)
#             token = access_token.create_access_token(
#                 data={"sub": form_data.phone_number},
#                 expires_delta=access_token_expires)
#             return JSONResponse(status_code=200,
#                                 content={"access_token": token,
#                                          "token_type": "Bearer",
#                                          "phone_number":jsonable_encoder(form_data.phone_number)})

@router_login.get("/au_user", responses=response_schemas.user_response)
def get_user(user: schemas.UserSchemas = Depends(get_current_user)) -> JSONResponse:
    """ Return User"""
    print(user)
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(user))
