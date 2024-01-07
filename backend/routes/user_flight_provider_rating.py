from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from backend.crud.CRUDUserFlightProviderRating import crud_user_flight_provider_rating
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_user_flight_provider_rating = APIRouter()


@router_user_flight_provider_rating.post("/", responses=response_schemas.user_flight_provider_rating_create_response)
def create_user_flight_provider_rating(user_flight_provider_rating: schemas.UserFlightProviderRatingCreate,
                                       current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create User Flight Provider Rating"""
    if current_user.authorization == 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if current_user.authorization == 1 and current_user.user_id != user_flight_provider_rating.user_id:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_flight_provider_rating_create = crud_user_flight_provider_rating.create_user_flight_provider_rating(
        user_flight_provider_rating=user_flight_provider_rating)
    if user_flight_provider_rating_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "User Flight Provider Rating Created"})


@router_user_flight_provider_rating.put("/", responses=response_schemas.user_flight_provider_rating_update_response)
def update_user_flight_provider_rating(user_flight_provider_rating: schemas.UserFlightProviderRatingUpdate,
                                       current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update User Flight Provider Rating"""
    user_flight_provider_rating_get = crud_user_flight_provider_rating.get_user_flight_provider_rating(
        user_flight_provider_rating_id=user_flight_provider_rating.id)
    if current_user.user_id != user_flight_provider_rating_get.user_id:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_flight_provider_rating_update = crud_user_flight_provider_rating.update_user_flight_provider_rating(
        user_flight_provider_rating=user_flight_provider_rating)
    if user_flight_provider_rating_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "User Flight Provider Rating Updated"})


@router_user_flight_provider_rating.delete("/", responses=response_schemas.user_flight_provider_rating_delete_response)
def delete_user_flight_provider_rating(user_flight_provider_rating: schemas.UserFlightProviderRatingDelete,
                                       current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete User Flight Provider Rating"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    user_flight_provider_rating_delete = crud_user_flight_provider_rating.delete_user_flight_provider_rating(
        user_flight_provider_rating=user_flight_provider_rating)
    if user_flight_provider_rating_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "User Flight Provider Rating Deleted"})


@router_user_flight_provider_rating.get("/", responses=response_schemas.user_flight_provider_rating_get_response)
def get_user_flight_provider_rating(user_flight_provider_rating_id,
                                    current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Get User Flight Provider Rating by user_flight_provider_rating_id"""
    user_flight_provider_rating_get = crud_user_flight_provider_rating.get_user_flight_provider_rating(
        user_flight_provider_rating_id=user_flight_provider_rating_id)
    if user_flight_provider_rating_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(user_flight_provider_rating_get))


@router_user_flight_provider_rating.get("/flight_provider_id", responses=response_schemas.user_flight_provider_rating_get_all_response)
def get_all_user_flight_provider_rating_by_flight_provider_id(flight_provider_id: str) -> JSONResponse:
    """ Get All User Flight Provider Ratings"""
    user_flight_provider_rating_get_all = crud_user_flight_provider_rating.get_all_user_flight_provider_rating_by_flight_provider_id(
        flight_provider_id=flight_provider_id)
    if user_flight_provider_rating_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(user_flight_provider_rating_get_all))


@router_user_flight_provider_rating.get("/user_id", responses=response_schemas.user_flight_provider_rating_get_all_response)
def get_all_user_flight_provider_rating_by_user_id(user_id: str) -> JSONResponse:
    """ Get All User Flight Provider Ratings"""
    user_flight_provider_rating_get_all = crud_user_flight_provider_rating.get_all_user_flight_provider_rating_by_user_id(
        user_id=user_id)
    if user_flight_provider_rating_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(user_flight_provider_rating_get_all))


