from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.crud.CRUDHotelService import crud_hotel_service
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_hotel_service = APIRouter()


@router_hotel_service.post("/", responses=response_schemas.hotel_service_create_response)
def create_hotel_service(hotel_service: schemas.HotelServiceCreate,
                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Hotel Service"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    hotel_service_create = crud_hotel_service.create_hotel_service(hotel_service=hotel_service)
    if hotel_service_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Hotel Service Created"})


@router_hotel_service.put("/", responses=response_schemas.hotel_service_update_response)
def update_hotel_service(hotel_service: schemas.HotelServiceUpdate,
                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Hotel Service"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    hotel_service_update = crud_hotel_service.update_hotel_service(hotel_service=hotel_service)
    if hotel_service_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Hotel Service Updated"})


@router_hotel_service.delete("/", responses=response_schemas.hotel_service_delete_response)
def delete_hotel_service(hotel_service: schemas.HotelServiceDelete,
                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Hotel Service"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    hotel_service_delete = crud_hotel_service.delete_hotel_service(hotel_service=hotel_service)
    if hotel_service_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Hotel Service Deleted"})


@router_hotel_service.get("/", responses=response_schemas.hotel_service_get_response)
def get_hotel_service(hotel_service_id) -> JSONResponse:
    """ Get Hotel Service"""
    hotel_service_get = crud_hotel_service.get_hotel_service(hotel_service_id=hotel_service_id)
    if hotel_service_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"hotel_service": jsonable_encoder(hotel_service_get)})


@router_hotel_service.get("/hotel-id", responses=response_schemas.hotel_service_all_response)
def get_hotel_service_by_hotel_id(hotel_id) -> JSONResponse:
    """ Get Hotel Service in a hotel"""
    hotel_service_get = crud_hotel_service.get_all_hotel_service_by_hotel_id(hotel_id=hotel_id)
    if hotel_service_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200,
                        content={"hotel_service": jsonable_encoder(hotel_service_get)})


# @router_hotel_service.get("/filter", responses=response_schemas.hotel_service_all_response)
# def get_all_hotel_service(city_hotel: str, name_hotel, page_number: int = 1, page_size: int = 10) -> JSONResponse:
#     """ Get All Hotel Service"""
#     hotel_service_all = crud_hotel_service.get_hotel_service_filter(page_number=page_number, page_size=page_size,
#                                                                     city_hotel=city_hotel, name_hotel=name_hotel)
#     if hotel_service_all is None:
#         return JSONResponse(status_code=400,
#                             content={"detail": "Bad Request"})
#     return JSONResponse(status_code=200,
#                         content={"hotel_service": jsonable_encoder(hotel_service_all)})
