from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDTourBooking import crud_tour_booking

from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_tour_booking = APIRouter()


@router_tour_booking.post("/", responses=response_schemas.tour_booking_create_response)
def create_tour_booking(tour_booking: schemas.TourBookingCreate,
                        current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Tour Booking"""
    if current_user.user_id != tour_booking.user_id and current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_booking_create = crud_tour_booking.create_tour_booking(tour_booking=tour_booking)
    if tour_booking_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Tour Booking Created"})


@router_tour_booking.put("/", responses=response_schemas.tour_booking_update_response)
def update_tour_booking(tour_booking: schemas.TourBookingUpdate,
                        current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Tour Booking"""
    if current_user.user_id != tour_booking.user_id and current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_booking_update = crud_tour_booking.update_tour_booking(tour_booking=tour_booking)
    if tour_booking_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Tour Booking Updated"})


@router_tour_booking.delete("/", responses=response_schemas.tour_booking_delete_response)
def delete_tour_booking(tour_booking: schemas.TourBookingDelete,
                        current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Tour Booking"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_booking_delete = crud_tour_booking.delete_tour_booking(tour_booking=tour_booking)
    if tour_booking_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Tour Booking Deleted"})


@router_tour_booking.get("/", responses=response_schemas.tour_booking_get_response)
def get_tour_booking(tour_booking_id, current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Get Tour Booking by tour_booking_id"""
    tour_booking_get = crud_tour_booking.get_tour_booking(tour_booking_id=tour_booking_id)
    if tour_booking_get.user_id != current_user.user_id and current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    if tour_booking_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"tour_booking": jsonable_encoder(tour_booking_get)})


@router_tour_booking.get("/tour-date-id", responses=response_schemas.all_tour_booking_response)
def get_all_tour_booking_by_tour_date_id(tour_date_id,
                                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Get all Tour Booking in a Tour Date by tour_date_id"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_booking_get_all = crud_tour_booking.get_all_tour_booking_by_tour_date_id(tour_date_id=tour_date_id)
    if tour_booking_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"tour_booking": jsonable_encoder(tour_booking_get_all)})


@router_tour_booking.get("/user-id", responses=response_schemas.all_tour_booking_response)
def get_all_tour_booking_by_user_id(user_id,
                                    current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Get all Tour Booking in a Tour Date by tour_date_id"""
    if current_user.authorization < 2 and current_user.user_id != user_id:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    tour_booking_get_all = crud_tour_booking.get_all_tour_booking_by_user_id(user_id=user_id)
    if tour_booking_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"tour_booking": jsonable_encoder(tour_booking_get_all)})

# @router_tour_booking.get("/all", responses=response_schemas.all_tour_booking_response)
# def get_all_tour_booking(current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
#     """ Get all Tour Booking"""
#     if current_user.authorization < 2:
#         return JSONResponse(status_code=401,
#                             content={"detail": "Unauthorized"})
#     tour_booking_get_all = crud_tour_booking.get_all_tour_booking()
#     if tour_booking_get_all is None:
#         return JSONResponse(status_code=400,
#                             content={"detail": "Bad Request"})
#     return JSONResponse(status_code=200, content={"tour_booking": jsonable_encoder(tour_booking_get_all)})
