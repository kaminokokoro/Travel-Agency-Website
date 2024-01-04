from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDTourDate import crud_tour_date

from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_tour_date = APIRouter()


@router_tour_date.post("/", responses=response_schemas.tour_date_create_response)
def create_tour_date(tour_date: schemas.TourDateCreate,
                     current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Tour Date"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_date_create = crud_tour_date.create_tour_date(tour_date=tour_date)
    if tour_date_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Tour Date Created"})


@router_tour_date.put("/", responses=response_schemas.tour_date_update_response)
def update_tour_date(tour_date: schemas.TourDateUpdate,
                     current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Tour Date"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_date_update = crud_tour_date.update_tour_date(tour_date=tour_date)
    if tour_date_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Tour Date Updated"})


@router_tour_date.delete("/", responses=response_schemas.tour_date_delete_response)
def delete_tour_date(tour_date: schemas.TourDateDelete,
                     current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Tour Date"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_date_delete = crud_tour_date.delete_tour_date(tour_date=tour_date)
    if tour_date_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Tour Date Deleted"})


@router_tour_date.get("/", responses=response_schemas.tour_date_get_response)
def get_tour_date(tour_date_id) -> JSONResponse:
    """ Get Tour Date by tour_date_id"""
    tour_date_get = crud_tour_date.get_tour_date_by_id(tour_date_id=tour_date_id)
    if tour_date_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(tour_date_get))


@router_tour_date.get("/all", responses=response_schemas.all_tour_date_response)
def get_tour_date_by_tour_id(tour_id) -> JSONResponse:
    """ Get all Tour Date in a Tour by tour_id"""
    tour_date_get_all = crud_tour_date.get_tour_date_by_tour_id_(tour_id=tour_id)
    if tour_date_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(tour_date_get_all))


@router_tour_date.get("/all/available", responses=response_schemas.all_tour_date_response)
def get_tour_date_by_tour_id(tour_id) -> JSONResponse:
    """ Get all Tour Date available in a Tour by tour_id"""
    tour_date_get_all = crud_tour_date.get_tour_date_from_now_by_tour_id(tour_id=tour_id)
    if tour_date_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(tour_date_get_all))
