from sqlalchemy.exc import SQLAlchemyError
from backend.db.db import session_scope
from backend.db.model import TourBooking, generate_uuid, UserRatingTour
from backend.util import schemas


class CRUDTourBooking:

        def create_tour_booking(self, tour_booking: schemas.TourBookingCreate) -> TourBooking:
            """Create Tour Booking"""
            try:
                with session_scope() as db:
                    tour_booking_db = TourBooking(id=generate_uuid(),
                                                user_id=tour_booking.user_id)
                    tour_booking_db.user_card_id = tour_booking.user_card_id
                    tour_booking_db.tour_date_id = tour_booking.tour_date_id
                    tour_booking_db.number_of_adult = tour_booking.number_of_adult
                    tour_booking_db.number_of_child = tour_booking.number_of_child
                    tour_booking_db.payment_time = tour_booking.payment_time
                    tour_booking_db.payment_status = tour_booking.payment_status
                    tour_booking_db.payment_description = tour_booking.payment_description
                    db.add(tour_booking_db)
                    db.commit()
                    db.refresh(tour_booking_db)
                    return tour_booking_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def update_tour_booking(self, tour_booking: schemas.TourBookingUpdate) -> TourBooking:
            try:
                with session_scope() as db:
                    tour_booking_db = db.query(TourBooking).filter(TourBooking.id == tour_booking.id).first()
                    if tour_booking_db is None:
                        return None
                    else:
                        tour_booking_db.user_id = tour_booking.user_id
                        tour_booking_db.user_card_id = tour_booking.user_card_id
                        tour_booking_db.tour_date_id = tour_booking.tour_date_id
                        tour_booking_db.number_of_adult = tour_booking.number_of_adult
                        tour_booking_db.number_of_child = tour_booking.number_of_child
                        tour_booking_db.payment_time = tour_booking.payment_time
                        tour_booking_db.payment_status = tour_booking.payment_status
                        tour_booking_db.payment_description = tour_booking.payment_description
                        db.commit()
                        db.refresh(tour_booking_db)
                        return tour_booking_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def delete_tour_booking(self, tour_booking: schemas.TourBookingDelete) -> TourBooking:
            try:
                with session_scope() as db:
                    tour_booking_db = db.query(TourBooking).filter(TourBooking.id == tour_booking.id).first()
                    if tour_booking_db is None:
                        return None
                    else:
                        db.delete(tour_booking_db)
                        db.commit()
                        return tour_booking_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def get_tour_booking(self, tour_booking_id) -> TourBooking:
            try:
                with session_scope() as db:
                    tour_booking_db = db.query(TourBooking).filter(TourBooking.id == tour_booking_id).first()
                    if tour_booking_db is None:
                        return None
                    else:
                        return tour_booking_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def get_all_tour_booking_by_user_id(self, user_id) -> TourBooking:
            try:
                with session_scope() as db:
                    tour_booking_db = db.query(TourBooking).filter(TourBooking.user_id == user_id).all()
                    if tour_booking_db is None:
                        return None
                    else:
                        return tour_booking_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def get_all_tour_booking_by_tour_date_id(self, tour_date_id) -> TourBooking:
            try:
                with session_scope() as db:
                    tour_booking_db = db.query(TourBooking).filter(TourBooking.tour_date_id == tour_date_id).all()
                    if tour_booking_db is None:
                        return None
                    else:
                        return tour_booking_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None


crud_tour_booking = CRUDTourBooking()