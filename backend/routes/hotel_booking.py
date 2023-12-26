from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDHotelBooking import crud_hotel_booking
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_hotel_booking = APIRouter()


@router_hotel_booking.post("/", responses=response_schemas.hotel_booking_create_response)
def create_hotel_booking(hotel_booking: schemas.HotelBookingCreate,
                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Hotel Booking"""
    if current_user.authorization == 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if current_user.id != hotel_booking.user_id and current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    hotel_booking_create = crud_hotel_booking.create_hotel_booking(hotel_booking=hotel_booking)
    if hotel_booking_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Hotel Booking Created"})

@router_hotel_booking.put("/", responses=response_schemas.hotel_booking_update_response)
def update_hotel_booking(hotel_booking: schemas.HotelBookingUpdate,
                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Hotel Booking"""
    if current_user.id != hotel_booking.user_id and current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    hotel_booking_update = crud_hotel_booking.update_hotel_booking(hotel_booking=hotel_booking)
    if hotel_booking_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Hotel Booking Updated"})

@router_hotel_booking.delete("/", responses=response_schemas.hotel_booking_delete_response)
def delete_hotel_booking(hotel_booking: schemas.HotelBookingDelete,
                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Hotel Booking"""
    if current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    hotel_booking_delete = crud_hotel_booking.delete_hotel_booking(hotel_booking=hotel_booking)
    if hotel_booking_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Hotel Booking Deleted"})

@router_hotel_booking.get("/", responses=response_schemas.hotel_booking_get_response)
def get_hotel_booking(hotel_booking_id,current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Get Hotel Booking"""

    hotel_booking_get = crud_hotel_booking.get_hotel_booking(hotel_booking_id=hotel_booking_id)
    if current_user.id != hotel_booking_get.user_id and current_user.authorization == 1:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if hotel_booking_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"hotel_booking": jsonable_encoder(hotel_booking_get)})


