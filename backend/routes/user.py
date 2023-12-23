from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDUser import crud_user
from backend.crud.CRUDlogin import crud_login
from backend.util import response_schemas,schemas
from backend.util.deps import get_current_user

router_user = APIRouter()

@router_user.post("/customer",responses=response_schemas.user_create_response)
def create_customer(user: schemas.UserSchemas) -> JSONResponse:
    """ Create Customer User"""
    db_user = crud_user.get_user_by_phone_number(phone_number=user.phone_number)
    if db_user is None:
        if user.authorization != 1:
            user.authorization = 1
        user_create=crud_user.create_user(user=user)
        if user_create is None:
            return JSONResponse(status_code=400,
                                content={"detail": "Bad Request"})
        return JSONResponse(status_code=200,
                            content={"message": "User Created"})
    else:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})


@router_user.post("/agent_or_admin",responses=response_schemas.user_create_response)
def create_user(user: schemas.UserSchemas,current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Agent or Admin User"""
    db_user = crud_user.get_user_by_phone_number(phone_number=user.phone_number)
    if db_user is None:
        if current_user.authorization <=2 and user.authorization==3:
            return JSONResponse(status_code=401,
                                content={"detail": "Unauthorized"})
        if current_user.authorization <2 and user.authorization==2:
            return JSONResponse(status_code=401,
                                content={"detail": "Unauthorized"})
        user_create=crud_user.create_user(user=user)
        if user_create is None:
            return JSONResponse(status_code=400,
                                content={"detail": "Bad Request"})
        return JSONResponse(status_code=200,
                            content={"message": "User Created"})
    else:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})

@router_user.get("/",responses=response_schemas.user_response)
def get_all_user(page_number:int = 1,page_size:int=10,current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Return All User"""
    if current_user.authorization <2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    users=crud_user.get_all_user(page_number=page_number,page_size=page_size)
    if users is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"users": jsonable_encoder(users)})



@router_user.put("/password",responses=response_schemas.user_password_update_response)
def update_user_password(user:schemas.UserUpdatePassword) -> JSONResponse:
    """ Update User Password"""
    db_user = crud_user.get_user_by_phone_number(phone_number=user.phone_number)
    if db_user is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    is_password_correct = crud_login.check_username_password(
        phone_number=user.phone_number,
        password=user.password)
    if is_password_correct is False:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    user_update=crud_user.update_user_password(user_id=db_user.id,new_password=user.new_password)
    if user_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"message": "Password Updated"})
@router_user.delete("/account",responses=response_schemas.user_delete_response)
def delete_user_account(phone_number,current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete User Account For Admin and Agent"""
    if current_user.authorization <2 :
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user=crud_user.get_user_by_phone_number(phone_number=phone_number)
    if user is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    if current_user.authorization <2 and user.authorization==2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if current_user.authorization <3 and user.authorization==3:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_delete=crud_user.delete_user_account(user_id=user.id)
    if user_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return (JSONResponse(status_code=200,
                        content={"message": "Account Deleted"})            )


@router_user.get("/profile",responses=response_schemas.user_profile_response)
def get_user_profile(current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Return User Profile"""
    
    user_profile=crud_user.get_user_profile(user_id=current_user.id)
    if user_profile is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"user_profile": jsonable_encoder(user_profile)})

@router_user.put("/profile",responses=response_schemas.user_profile_update_response)
def update_user_profile(user_profile: schemas.UserProfileSchemas,current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update User Profile"""
    user_profile_update=crud_user.update_user_profile(user_id=current_user.id,user_profile_schemas=user_profile)
    if user_profile_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"message": "Profile Updated"})

@router_user.post("/profile",responses=response_schemas.user_profile_create_response)
def create_user_profile(user_profile: schemas.UserProfileSchemas,current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create User Profile"""
    user_profile_create=crud_user.create_user_profile(user_id=current_user.id,user_profile_schemas=user_profile)
    if user_profile_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"message": "Profile Created"})

@router_user.get("/card",responses=response_schemas.user_card_response)
def get_user_card(current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Return User Card"""
    user_card=crud_user.get_all_user_card(user_id=current_user.id)
    if user_card is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"user_card": jsonable_encoder(user_card)})

@router_user.put("/card",responses=response_schemas.user_card_update_response)
def update_user_card(user_card: schemas.UserCardUpdateSchemas,current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update User Card"""
    user_card_update=crud_user.update_user_card(user_id=current_user.id,user_card_schemas=user_card,card_id=user_card.id)
    if user_card_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"message": "Card Updated"})

@router_user.post("/card",responses=response_schemas.user_card_create_response)
def create_user_card(user_card: schemas.UserCardSchemas,current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create User Card"""
    user_card_create=crud_user.create_user_card(user_id=current_user.id,user_card_schemas=user_card)
    if user_card_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"message": "Card Created"})

@router_user.delete("/card",responses=response_schemas.user_card_delete_response)
def delete_user_card(user_card:schemas.UserCardID,current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete User Card"""
    user_card_delete=crud_user.delete_user_card(user_id=current_user.id,card_id=user_card.id)
    if user_card_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"message": "Card Deleted"})

