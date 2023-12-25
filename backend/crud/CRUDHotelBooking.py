from backend.db.model import HotelBooking, generate_uuid
from backend.util import schemas
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from backend.db.db import session_scope


class CRUDHotelBooking:
    def create_hotel_booking(self, hotel_booking: schemas.HotelBookingCreate) -> HotelBooking:
        """Create Hotel Booking"""
        try:
            with session_scope() as db:
                hotel_booking_db = HotelBooking(id=generate_uuid(),
                                                user_id=hotel_booking.user_id, check_in=hotel_booking.check_in,
                                                check_out=hotel_booking.check_out,
                                                number_of_room=hotel_booking.number_of_room,
                                                user_card_id=hotel_booking.user_card_id,
                                                hotel_services_id=hotel_booking.hotel_services_id,
                                                payment_description=hotel_booking.payment_description,
                                                payment_time=hotel_booking.payment_time,
                                                payment_status=hotel_booking.payment_status,)
                db.add(hotel_booking_db)
                db.commit()
                db.refresh(hotel_booking_db)
                return hotel_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def update_hotel_booking(self, hotel_booking: schemas.HotelBookingUpdate) -> HotelBooking:
        try:
            with session_scope() as db:
                hotel_booking_db = db.query(HotelBooking).filter(HotelBooking.id == hotel_booking.id).first()
                if hotel_booking_db is None:
                    return None
                else:
                    hotel_booking_db.user_id = hotel_booking.user_id
                    hotel_booking_db.check_in = hotel_booking.check_in
                    hotel_booking_db.check_out = hotel_booking.check_out
                    hotel_booking_db.number_of_room = hotel_booking.number_of_room
                    hotel_booking_db.user_card_id = hotel_booking.user_card_id
                    hotel_booking_db.hotel_services_id = hotel_booking.hotel_services_id
                    hotel_booking_db.payment_description = hotel_booking.payment_description
                    hotel_booking_db.payment_time = hotel_booking.payment_time
                    hotel_booking_db.payment_status = hotel_booking.payment_status
                    db.commit()
                    db.refresh(hotel_booking_db)
                    return hotel_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def delete_hotel_booking(self, hotel_booking: schemas.HotelBookingDelete) -> HotelBooking:
        try:
            with session_scope() as db:
                hotel_booking_db = db.query(HotelBooking).filter(HotelBooking.id == hotel_booking.id).first()
                if hotel_booking_db is None:
                    return None
                else:
                    db.delete(hotel_booking_db)
                    db.commit()
                    return hotel_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_hotel_booking(self, hotel_booking_id) -> HotelBooking:
        try:
            with session_scope() as db:
                hotel_booking_db = db.query(HotelBooking).filter(and_(HotelBooking.id == hotel_booking_id)).first()
                return hotel_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_all_hotel_booking_by_user_id(self,user_id:str, page_number: int = 1, page_size: int = 10) -> HotelBooking:
        try:
            with session_scope() as db:
                hotel_booking_db = db.query(HotelBooking).filter(and_(HotelBooking.user_id == user_id)).offset((page_number - 1) * page_size).limit(page_size).all()
                return hotel_booking_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None
