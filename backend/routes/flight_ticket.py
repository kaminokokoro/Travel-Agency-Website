from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from backend.crud.CRUDFlightTicket import crud_flight_ticket
from backend.util import response_schemas, schemas
from backend.util.deps import get_current_user

router_flight_ticket = APIRouter()


@router_flight_ticket.post("/", responses=response_schemas.flight_ticket_create_response)
def create_flight_ticket(flight_ticket: schemas.FlightTicketCreate,
                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Create Flight Ticket"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_ticket_create = crud_flight_ticket.create_flight_ticket(flight_ticket=flight_ticket)
    if flight_ticket_create is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Flight Ticket Created"})


@router_flight_ticket.put("/", responses=response_schemas.flight_ticket_update_response)
def update_flight_ticket(flight_ticket: schemas.FlightTicketUpdate,
                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Update Flight Ticket"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_ticket_update = crud_flight_ticket.update_flight_ticket(flight_ticket=flight_ticket)
    if flight_ticket_update is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"message": "Flight Ticket Updated"})


@router_flight_ticket.delete("/", responses=response_schemas.flight_ticket_delete_response)
def delete_flight_ticket(flight_ticket: schemas.FlightTicketDelete,
                         current_user: schemas.UserVerify = Depends(get_current_user)) -> JSONResponse:
    """ Delete Flight Ticket"""
    if current_user.authorization < 2:
        return JSONResponse(status_code=401,
                            content={"detail": "Unauthorized"})
    flight_ticket_delete = crud_flight_ticket.delete_flight_ticket(flight_ticket=flight_ticket)
    if flight_ticket_delete is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content={"detail": "Flight Ticket Deleted"})


@router_flight_ticket.get("/", responses=response_schemas.flight_ticket_get_response)
def get_flight_ticket(flight_ticket_id) -> JSONResponse:
    """ Get Flight Ticket by flight_ticket_id"""
    flight_ticket_get = crud_flight_ticket.get_flight_ticket(flight_ticket_id=flight_ticket_id)
    if flight_ticket_get is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(flight_ticket_get))


@router_flight_ticket.get("/all", responses=response_schemas.flight_ticket_get_all_response)
def get_all_flight_ticket_by_flight_id(flight_id: str) -> JSONResponse:
    """ Get All Flight Ticket"""
    flight_ticket_get_all = crud_flight_ticket.get_all_flight_ticket_by_flight_id(flight_id=flight_id)
    if flight_ticket_get_all is None:
        return JSONResponse(status_code=400,
                            content={"detail": "Bad Request"})
    return JSONResponse(status_code=200, content=jsonable_encoder(flight_ticket_get_all))
