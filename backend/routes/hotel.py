from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDHotel import crud_hotel
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_hotel = APIRouter()


@router_hotel.post("/", responses=response_schemas.hotel_create_response)
def create_hotel(hotel: schemas.HotelCreate,
                 current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Hotel"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    hotel_create = crud_hotel.create_hotel(hotel=hotel)
    if hotel_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Hotel Created"})


@router_hotel.put("/", responses=response_schemas.hotel_update_response)
def update_hotel(hotel: schemas.HotelUpdate,
                 current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Hotel"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    hotel_update = crud_hotel.update_hotel(hotel=hotel)
    if hotel_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Hotel Updated"})


@router_hotel.delete("/", responses=response_schemas.hotel_delete_response)
def delete_hotel(hotel: schemas.HotelDelete,
                 current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Hotel"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    hotel_delete = crud_hotel.delete_hotel(hotel=hotel)
    if hotel_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Hotel Deleted"})


@router_hotel.get("/", responses=response_schemas.hotel_get_response)
def get_hotel(hotel_id) -> JSONResponse:
    """ Get Hotel"""
    hotel_get = crud_hotel.get_hotel(hotel_id=hotel_id)
    if hotel_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"hotel": jsonable_encoder(hotel_get)})


@router_hotel.get("/all", responses=response_schemas.hotel_all_response)
def get_all_hotel(page_number: int = 1, page_size: int = 10) -> JSONResponse:
    """ Get All Hotel sort by rating"""
    hotel_all = crud_hotel.get_all_hotel(page_number=page_number, page_size=page_size)
    if hotel_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"hotel": jsonable_encoder(hotel_all)})

# @router_hotel.get("/filter",responses=response_schemas.hotel_all_response)
# def get_all_hotel(page_number:int = 1,page_size:int=10) -> JSONResponse:
#     """ Get All Hotel"""
#     # hotel_all=crud_hotel.get_all_hotel(page_number=page_number,page_size=page_size)
#     if hotel_all is None:
#         return JSONResponse(status_code=400,
#                             content={"detail": "Bad Request"})
#     return JSONResponse(status_code=200,content={"hotel": jsonable_encoder(hotel_all)})
