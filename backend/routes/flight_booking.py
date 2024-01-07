from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from backend.crud.CRUDFlightBooking import crud_flight_booking
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_flight_booking = APIRouter()


@router_flight_booking.post("/", responses=response_schemas.flight_booking_create_response)
def create_flight_booking(flight_booking: schemas.FlightBookingCreate,
                          current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Flight Booking"""
    if current_user.authorization == 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if current_user.authorization == 1 and current_user.user_id != flight_booking.user_id:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_booking_create = crud_flight_booking.create_flight_booking(flight_booking=flight_booking)
    if flight_booking_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Flight Booking Created"})


@router_flight_booking.put("/", responses=response_schemas.flight_booking_update_response)
def update_flight_booking(flight_booking: schemas.FlightBookingUpdate,
                          current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Flight Booking"""
    flight_booking_get = crud_flight_booking.get_flight_booking(flight_booking_id=flight_booking.id)
    if current_user.authorization == 1 and current_user.user_id != flight_booking_get.user_id:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_booking_update = crud_flight_booking.update_flight_booking(flight_booking=flight_booking)
    if flight_booking_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Flight Booking Updated"})


@router_flight_booking.delete("/", responses=response_schemas.flight_booking_delete_response)
def delete_flight_booking(flight_booking: schemas.FlightBookingDelete,
                          current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Flight Booking"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_booking_delete = crud_flight_booking.delete_flight_booking(flight_booking=flight_booking)
    if flight_booking_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Flight Booking Deleted"})


@router_flight_booking.get("/", responses=response_schemas.flight_booking_get_response)
def get_flight_booking(flight_booking_id, current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Get Flight Booking by flight_booking_id"""
    flight_booking_get = crud_flight_booking.get_flight_booking(flight_booking_id=flight_booking_id)
    if current_user.authorization == 1 and current_user.user_id != flight_booking_get.user_id:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if flight_booking_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(flight_booking_get))


@router_flight_booking.get("/all", responses=response_schemas.flight_booking_get_all_response)
def get_all_flight_booking_by_user_id(user_id: str,
                                      current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Get all Flight Booking by user_id"""
    flight_booking_get_all = crud_flight_booking.get_flight_booking_by_user_id(user_id=user_id)
    if current_user.authorization == 1 and current_user.user_id != user_id:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if flight_booking_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(flight_booking_get_all))
