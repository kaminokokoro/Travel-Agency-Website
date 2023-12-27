from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDUserHotelRating import crud_user_hotel_rating
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_user_hotel_rating = APIRouter()


@router_user_hotel_rating.post("/", responses=response_schemas.user_hotel_rating_create_response)
def create_user_hotel_rating(user_hotel_rating: schemas.UserHotelRatingCreate,
                             current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create User Hotel Rating"""
    if current_user.authorization == 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if current_user.id != user_hotel_rating.user_id and current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_hotel_rating_create = crud_user_hotel_rating.create_user_hotel_rating(user_hotel_rating=user_hotel_rating)
    if user_hotel_rating_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "User Hotel Rating Created"})

@router_user_hotel_rating.put("/", responses=response_schemas.user_hotel_rating_update_response)
def update_user_hotel_rating(user_hotel_rating: schemas.UserHotelRatingUpdate,
                             current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update User Hotel Rating"""
    if current_user.id != user_hotel_rating.user_id and current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_hotel_rating_update = crud_user_hotel_rating.update_user_hotel_rating(user_hotel_rating=user_hotel_rating)
    if user_hotel_rating_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "User Hotel Rating Updated"})

@router_user_hotel_rating.delete("/", responses=response_schemas.user_hotel_rating_delete_response)
def delete_user_hotel_rating(user_hotel_rating: schemas.UserHotelRatingDelete,
                             current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete User Hotel Rating"""
    user_hotel_rating_get = crud_user_hotel_rating.get_user_hotel_rating(user_hotel_rating_id=user_hotel_rating.id)
    if current_user.id != user_hotel_rating_get.user_id and current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_hotel_rating_delete = crud_user_hotel_rating.delete_user_hotel_rating(user_hotel_rating=user_hotel_rating)

    if user_hotel_rating_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "User Hotel Rating Deleted"})

@router_user_hotel_rating.get("/", responses=response_schemas.user_hotel_rating_get_response)
def get_user_hotel_rating(user_hotel_rating_id) -> JSONResponse:
    """ Get User Hotel Rating by id"""
    user_hotel_rating_get = crud_user_hotel_rating.get_user_hotel_rating(user_hotel_rating_id=user_hotel_rating_id)
    if user_hotel_rating_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"Hotel Rating": jsonable_encoder(user_hotel_rating_get)})

@router_user_hotel_rating.get("/all/hotel", responses=response_schemas.user_hotel_rating_all_response)
def get_user_hotel_rating_by_hotel(hotel_id) -> JSONResponse:
    """ Get User Hotel Rating by hotel_id"""
    user_hotel_rating_get = crud_user_hotel_rating.get_all_user_hotel_rating_by_hotel_id(hotel_id=hotel_id)
    if user_hotel_rating_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={ "Hotel Rating": jsonable_encoder(user_hotel_rating_get)})

@router_user_hotel_rating.get("/all/user", responses=response_schemas.user_hotel_rating_all_response)
def get_user_hotel_rating_by_user(user_id) -> JSONResponse:
    """ Get User Hotel Rating by user_id"""
    user_hotel_rating_get = crud_user_hotel_rating.get_all_user_hotel_rating_by_user_id(user_id=user_id)
    if user_hotel_rating_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"Hotel Rating": jsonable_encoder(user_hotel_rating_get)})