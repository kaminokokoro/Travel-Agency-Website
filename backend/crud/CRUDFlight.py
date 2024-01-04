from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_, func
from backend.db.db import session_scope
from backend.db.model import Flight, generate_uuid
from backend.util import schemas


class CRUDFlight:

    def create_flight(self, flight: schemas.FlightCreate) -> Flight:
        """Create Flight"""
        try:
            with session_scope() as db:
                flight_db = Flight(id=generate_uuid(), name=flight.name, departure=flight.departure,
                                   arrival=flight.arrival, departure_time=flight.departure_time,
                                   arrival_time=flight.arrival_time, price=flight.price)
                db.add(flight_db)
                db.commit()
                db.refresh(flight_db)
                return flight_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def update_flight(self, flight: schemas.FlightUpdate) -> Flight:
        try:
            with session_scope() as db:
                flight_db = db.query(Flight).filter(Flight.id == flight.id).first()
                if flight_db is None:
                    return None
                else:
                    flight_db.name = flight.name
                    flight_db.departure = flight.departure
                    flight_db.arrival = flight.arrival
                    flight_db.departure_time = flight.departure_time
                    flight_db.arrival_time = flight.arrival_time
                    flight_db.price = flight.price
                    db.commit()
                    db.refresh(flight_db)
                    return flight_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def delete_flight(self, flight: schemas.FlightDelete) -> Flight:
        try:
            with session_scope() as db:
                flight_db = db.query(Flight).filter(Flight.id == flight.id).first()
                if flight_db is None:
                    return None
                else:
                    db.delete(flight_db)
                    db.commit()
                    return flight_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_flight(self, flight_id) -> Flight:
        try:
            with session_scope() as db:
                flight_db = db.query(Flight).filter(Flight.id == flight_id).first()
                if flight_db is None:
                    return None
                else:
                    return flight_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_all_flights_filter(self, departure_from, arrival_to, datetime_from, datetime_to, page_number: int,
                               page_size: int):
        try:
            with session_scope() as db:
                if datetime_from == "":
                    datetime_from = func.now()
                if datetime_to == "":
                    datetime_to = func.now() + func.interval(30, 'day')
                flight_db = db.query(Flight).filter(
                    and_(Flight.departure == departure_from, Flight.arrival == arrival_to,
                         Flight.departure_time >= datetime_from,
                         Flight.departure_time <= datetime_to)).limit(
                    page_size).offset((page_number - 1) * page_size).all()
                if flight_db is None:
                    return None
                return flight_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None


crud_flight = CRUDFlight()
