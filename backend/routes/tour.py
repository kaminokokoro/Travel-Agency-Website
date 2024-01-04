from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDTour import crud_tour
from backend.routes.tour_date import router_tour_date

from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_tour = APIRouter()
router_tour.include_router(router_tour_date, prefix="/date", tags=["tour_date"])

@router_tour.post("/", responses=response_schemas.tour_create_response)
def create_tour(tour: schemas.TourCreate,
                current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Tour"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_create = crud_tour.create_tour(tour=tour)
    if tour_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Tour Created"})


@router_tour.put("/", responses=response_schemas.tour_update_response)
def update_tour(tour: schemas.TourUpdate,
                current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Tour"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_update = crud_tour.update_tour(tour=tour)
    if tour_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Tour Updated"})


@router_tour.delete("/", responses=response_schemas.tour_delete_response)
def delete_tour(tour: schemas.TourDelete,
                current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Tour"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_delete = crud_tour.delete_tour(tour=tour)
    if tour_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Tour Deleted"})


@router_tour.get("/", responses=response_schemas.tour_get_response)
def get_tour(tour_id) -> JSONResponse:
    """ Get Tour by tour_id"""
    tour_get = crud_tour.get_tour(tour_id=tour_id)
    if tour_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(tour_get))


@router_tour.get("/filter", responses=response_schemas.tour_get_all_response, description="")
def get_all_tour(page_number: int = 1, page_size: int = 10, destination: str = "", name: str = "") -> JSONResponse:
    """ Get All filtered Tour"""
    tour_get_all = crud_tour.get_all_tour_filter(page_number=page_number, page_size=page_size, destination=destination,
                                                 name=name)
    if tour_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(tour_get_all))
