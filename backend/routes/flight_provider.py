from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from backend.crud.CRUDFlightProvider import crud_flight_provider
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_flight_provider = APIRouter()


@router_flight_provider.post("/", responses=response_schemas.flight_provider_create_response)
def create_flight_provider(flight_provider: schemas.FlightProviderCreate,
                           current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Flight Provider"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_provider_create = crud_flight_provider.create_flight_provider(flight_provider=flight_provider)
    if flight_provider_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Flight Provider Created"})

@router_flight_provider.put("/", responses=response_schemas.flight_provider_update_response)
def update_flight_provider(flight_provider: schemas.FlightProviderUpdate,
                           current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Flight Provider"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_provider_update = crud_flight_provider.update_flight_provider(flight_provider=flight_provider)
    if flight_provider_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Flight Provider Updated"})

@router_flight_provider.delete("/", responses=response_schemas.flight_provider_delete_response)
def delete_flight_provider(flight_provider: schemas.FlightProviderDelete,
                           current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Flight Provider"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_provider_delete = crud_flight_provider.delete_flight_provider(flight_provider=flight_provider)
    if flight_provider_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Flight Provider Deleted"})

@router_flight_provider.get("/", responses=response_schemas.flight_provider_get_response)
def get_flight_provider(flight_provider_id) -> JSONResponse:
    """ Get Flight Provider by flight_provider_id"""
    flight_provider_get = crud_flight_provider.get_flight_provider(flight_provider_id=flight_provider_id)
    if flight_provider_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(flight_provider_get))

@router_flight_provider.get("/all", responses=response_schemas.flight_provider_get_all_response)
def get_all_flight_provider() -> JSONResponse:
    """ Get All Flight Providers"""
    flight_provider_get_all = crud_flight_provider.get_all_flight_providers_by_rating()
    if flight_provider_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(flight_provider_get_all))