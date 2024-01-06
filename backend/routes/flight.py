from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDFlight import crud_flight

from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_flight = APIRouter()


@router_flight.post("/", responses=response_schemas.flight_create_response)
def create_flight(flight: schemas.FlightCreate,
                  current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Flight"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_create = crud_flight.create_flight(flight=flight)
    if flight_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Flight Created"})


@router_flight.put("/", responses=response_schemas.flight_update_response)
def update_flight(flight: schemas.FlightUpdate,
                  current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Flight"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_update = crud_flight.update_flight(flight=flight)
    if flight_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Flight Updated"})


@router_flight.delete("/", responses=response_schemas.flight_delete_response)
def delete_flight(flight: schemas.FlightDelete,
                  current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Flight"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_delete = crud_flight.delete_flight(flight=flight)
    if flight_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Flight Deleted"})


@router_flight.get("/", responses=response_schemas.flight_get_response)
def get_flight(flight_id) -> JSONResponse:
    """ Get Flight by flight_id"""
    flight_get = crud_flight.get_flight(flight_id=flight_id)
    if flight_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(flight_get))


@router_flight.get("/filter", responses=response_schemas.flight_get_all_response)
def get_all_flight(departure_from, arrival_to, page_num: int = 1, page_size: int = 10, datetime_from: str = "",
                   datetime_to: str = "") -> JSONResponse:
    """ Get all Flight"""
    flight_get_all = crud_flight.get_all_flights_filter(departure_from=departure_from, arrival_to=arrival_to,
                                                        page_num=page_num, page_size=page_size,
                                                        datetime_from=datetime_from, datetime_to=datetime_to)
    if flight_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(flight_get_all))


@router_flight.get("/all", responses=response_schemas.flight_get_all_response)
def get_all_flight(page_num: int = 1, page_size: int = 10) -> JSONResponse:
    """ Get all Flight"""
    flight_get_all = crud_flight.get_all_flights(page_num=page_num, page_size=page_size)
    if flight_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(flight_get_all))
