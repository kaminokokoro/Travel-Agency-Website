from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_, func
from backend.db.db import session_scope
from backend.db.model import FlightTicket, generate_uuid
from backend.util import schemas


class CRUDFlightTicket:

        def create_flight_ticket(self, flight_ticket: schemas.FlightTicketCreate) -> FlightTicket:
            """Create Flight Ticket"""
            try:
                with session_scope() as db:
                    flight_ticket_db = FlightTicket(id=generate_uuid(),
                                                    flight_id=flight_ticket.flight_id)
                    flight_ticket_db.adult_price = flight_ticket.adult_price
                    flight_ticket_db.child_price = flight_ticket.child_price
                    flight_ticket_db.baby_price = flight_ticket.baby_price
                    flight_ticket_db.seat_class = flight_ticket.seat_class
                    flight_ticket_db.name = flight_ticket.name
                    flight_ticket_db.description = flight_ticket.description

                    db.add(flight_ticket_db)
                    db.commit()
                    db.refresh(flight_ticket_db)
                    return flight_ticket_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def update_flight_ticket(self, flight_ticket: schemas.FlightTicketUpdate) -> FlightTicket:
            try:
                with session_scope() as db:
                    flight_ticket_db = db.query(FlightTicket).filter(FlightTicket.id == flight_ticket.id).first()
                    if flight_ticket_db is None:
                        return None
                    else:
                        flight_ticket_db.adult_price = flight_ticket.adult_price
                        flight_ticket_db.child_price = flight_ticket.child_price
                        flight_ticket_db.baby_price = flight_ticket.baby_price
                        flight_ticket_db.seat_class = flight_ticket.seat_class
                        flight_ticket_db.name = flight_ticket.name
                        flight_ticket_db.description = flight_ticket.description
                        db.commit()
                        db.refresh(flight_ticket_db)
                        return flight_ticket_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None



        def delete_flight_ticket(self, flight_ticket: schemas.FlightTicketDelete) -> FlightTicket:
            try:
                with session_scope() as db:
                    flight_ticket_db = db.query(FlightTicket).filter(FlightTicket.id == flight_ticket.id).first()
                    if flight_ticket_db is None:
                        return None
                    else:
                        db.delete(flight_ticket_db)
                        db.commit()
                        return flight_ticket_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def get_flight_ticket(self, flight_ticket_id) -> FlightTicket:
            try:
                with session_scope() as db:
                    flight_ticket_db = db.query(FlightTicket).filter(FlightTicket.id == flight_ticket_id).first()
                    return flight_ticket_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def get_all_flight_ticket_by_flight_id(self, flight_id) -> FlightTicket:
            try:
                with session_scope() as db:
                    flight_ticket_db = db.query(FlightTicket).filter(FlightTicket.flight_id == flight_id).all()
                    return flight_ticket_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None


crud_flight_ticket = CRUDFlightTicket()