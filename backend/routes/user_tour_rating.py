from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDUserTourRating import crud_user_tour_rating
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user


router_user_tour_rating = APIRouter()


@router_user_tour_rating.post("/", responses=response_schemas.user_tour_rating_create_response)
def create_user_tour_rating(user_tour_rating: schemas.UserTourRatingCreate,
                            current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create User Tour Rating"""
    if current_user.authorization == 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if current_user.id != user_tour_rating.user_id and current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_tour_rating_create = crud_user_tour_rating.create_user_tour_rating(user_tour_rating=user_tour_rating)
    if user_tour_rating_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "User Tour Rating Created"})

@router_user_tour_rating.put("/", responses=response_schemas.user_tour_rating_update_response)
def update_user_tour_rating(user_tour_rating: schemas.UserTourRatingUpdate,
                            current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update User Tour Rating"""
    if current_user.id != user_tour_rating.user_id and current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_tour_rating_update = crud_user_tour_rating.update_user_tour_rating(user_tour_rating=user_tour_rating)
    if user_tour_rating_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "User Tour Rating Updated"})

@router_user_tour_rating.delete("/", responses=response_schemas.user_tour_rating_delete_response)
def delete_user_tour_rating(user_tour_rating: schemas.UserTourRatingDelete,
                            current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete User Tour Rating"""
    user_tour_rating_get = crud_user_tour_rating.get_user_tour_rating(user_tour_rating_id=user_tour_rating.id)
    if current_user.id != user_tour_rating_get.user_id and current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_tour_rating_delete = crud_user_tour_rating.delete_user_tour_rating(user_tour_rating=user_tour_rating)

    if user_tour_rating_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "User Tour Rating Deleted"})

@router_user_tour_rating.get("/", responses=response_schemas.user_tour_rating_get_response)
def get_user_tour_rating(user_tour_rating_id) -> JSONResponse:
    """ Get User Tour Rating by id"""
    user_tour_rating_get = crud_user_tour_rating.get_user_tour_rating(user_tour_rating_id=user_tour_rating_id)
    if user_tour_rating_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(user_tour_rating_get))

@router_user_tour_rating.get("/all/tour", responses=response_schemas.user_tour_rating_all_response)
def get_user_tour_rating_by_tour(tour_id) -> JSONResponse:
    """ Get User Tour Rating by tour_id"""
    user_tour_rating_get = crud_user_tour_rating.get_user_tour_rating_by_tour_id(tour_id=tour_id)
    if user_tour_rating_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(user_tour_rating_get))

@router_user_tour_rating.get("/all/user", responses=response_schemas.user_tour_rating_all_response)
def get_user_tour_rating_by_user(user_id) -> JSONResponse:
    """ Get User Tour Rating by user_id"""
    user_tour_rating_get = crud_user_tour_rating.get_user_tour_rating_by_user_id(user_id=user_id)
    if user_tour_rating_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(user_tour_rating_get))