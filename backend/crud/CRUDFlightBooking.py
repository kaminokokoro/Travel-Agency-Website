from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_
from backend.db.db import session_scope
from backend.db.model import FlightBooking, generate_uuid
from backend.util import schemas


class CRUDFlightBooking:
    def create_flight_booking(self, flight_booking: schemas.FlightBookingCreate) -> FlightBooking:
        """Create Flight Booking"""
        try:
            with session_scope() as db:
                flight_booking_db = FlightBooking(id=generate_uuid())
                flight_booking_db.user_id = flight_booking.user_id
                flight_booking_db.user_card_id = flight_booking.user_card_id
                flight_booking_db.departure_flight_ticket_id = flight_booking.departure_flight_ticket_id
                flight_booking_db.return_flight_ticket_id = flight_booking.return_flight_ticket_id
                flight_booking_db.payment_time = flight_booking.payment_time
                flight_booking_db.payment_status = flight_booking.payment_status
                flight_booking_db.payment_description = flight_booking.payment_description
                flight_booking_db.number_of_adult = flight_booking.number_of_adult
                flight_booking_db.number_of_child = flight_booking.number_of_child
                flight_booking_db.number_of_baby = flight_booking.number_of_baby

                db.add(flight_booking_db)
                db.commit()
                db.refresh(flight_booking_db)
                return flight_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def update_flight_booking(self, flight_booking: schemas.FlightBookingUpdate) -> FlightBooking:
        try:
            with session_scope() as db:
                flight_booking_db = db.query(FlightBooking).filter(FlightBooking.id == flight_booking.id).first()
                if flight_booking_db is None:
                    return None
                else:
                    flight_booking_db.user_id = flight_booking.user_id
                    flight_booking_db.user_card_id = flight_booking.user_card_id
                    flight_booking_db.departure_flight_ticket_id = flight_booking.departure_flight_ticket_id
                    flight_booking_db.return_flight_ticket_id = flight_booking.return_flight_ticket_id
                    flight_booking_db.payment_time = flight_booking.payment_time
                    flight_booking_db.payment_status = flight_booking.payment_status
                    flight_booking_db.payment_description = flight_booking.payment_description
                    flight_booking_db.number_of_adult = flight_booking.number_of_adult
                    flight_booking_db.number_of_child = flight_booking.number_of_child
                    flight_booking_db.number_of_baby = flight_booking.number_of_baby
                    db.commit()
                    db.refresh(flight_booking_db)
                    return flight_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def delete_flight_booking(self, flight_booking: schemas.FlightBookingDelete) -> FlightBooking:
        try:
            with session_scope() as db:
                flight_booking_db = db.query(FlightBooking).filter(FlightBooking.id == flight_booking.id).first()
                if flight_booking_db is None:
                    return None
                else:
                    db.delete(flight_booking_db)
                    db.commit()
                    return flight_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_flight_booking(self, flight_booking_id) -> FlightBooking:
        try:
            with session_scope() as db:
                flight_booking_db = db.query(FlightBooking).filter(FlightBooking.id == flight_booking_id).first()
                return flight_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_flight_booking_by_user_id(self, user_id) -> FlightBooking:
        try:
            with session_scope() as db:
                flight_booking_db = db.query(FlightBooking).filter(FlightBooking.user_id == user_id).all()
                return flight_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_all_flight_booking_by_flight_ticket_id(self, flight_ticket_id,page_num, page_size) -> FlightBooking:
        try:
            with session_scope() as db:
                flight_booking_db = db.query(FlightBooking).filter(
                    or_(FlightBooking.departure_flight_ticket_id == flight_ticket_id,
                        FlightBooking.return_flight_ticket_id == flight_ticket_id)).limit(page_size).offset(
                    (page_num - 1) * page_size).all()
                return flight_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None


crud_flight_booking = CRUDFlightBooking()