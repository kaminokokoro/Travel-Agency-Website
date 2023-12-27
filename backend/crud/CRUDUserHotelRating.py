from backend.db.model import UserRatingHotel, generate_uuid
from backend.util import schemas
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from backend.db.db import session_scope

class CRUDUserHotelRating:
    def create_user_hotel_rating(self, user_hotel_rating: schemas.UserHotelRatingCreate) -> UserRatingHotel:
        """Create User Hotel Rating"""
        try:
            with session_scope() as db:
                user_hotel_rating_db = UserRatingHotel(id=generate_uuid(),
                                                user_id=user_hotel_rating.user_id, hotel_id=user_hotel_rating.hotel_id,
                                                rating=user_hotel_rating.rating, comment=user_hotel_rating.comment)
                db.add(user_hotel_rating_db)
                db.commit()
                db.refresh(user_hotel_rating_db)
                return user_hotel_rating_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def update_user_hotel_rating(self, user_hotel_rating: schemas.UserHotelRatingUpdate) -> UserRatingHotel:
        try:
            with session_scope() as db:
                user_hotel_rating_db = db.query(UserRatingHotel).filter(UserRatingHotel.id == user_hotel_rating.id).first()
                if user_hotel_rating_db is None:
                    return None
                else:
                    user_hotel_rating_db.user_id = user_hotel_rating.user_id
                    user_hotel_rating_db.hotel_id = user_hotel_rating.hotel_id
                    user_hotel_rating_db.rating = user_hotel_rating.rating
                    user_hotel_rating_db.comment = user_hotel_rating.comment
                    db.commit()
                    db.refresh(user_hotel_rating_db)
                    return user_hotel_rating_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def delete_user_hotel_rating(self, user_hotel_rating: schemas.UserHotelRatingDelete) -> UserRatingHotel:
        try:
            with session_scope() as db:
                user_hotel_rating_db = db.query(UserRatingHotel).filter(UserRatingHotel.id == user_hotel_rating.id).first()
                if user_hotel_rating_db is None:
                    return None
                else:
                    db.delete(user_hotel_rating_db)
                    db.commit()
                    return user_hotel_rating_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_user_hotel_rating(self, user_hotel_rating_id) -> UserRatingHotel:
        try:
            with session_scope() as db:
                user_hotel_rating_db = db.query(UserRatingHotel).filter(UserRatingHotel.id == user_hotel_rating_id).first()
                if user_hotel_rating_db is None:
                    return None
                else:
                    return user_hotel_rating_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_all_user_hotel_rating_by_user_id(self, user_id) -> UserRatingHotel:
        try:
            with session_scope() as db:
                user_hotel_rating_db = db.query(UserRatingHotel).filter(UserRatingHotel.user_id == user_id).all()
                if user_hotel_rating_db is None:
                    return None
                else:
                    return user_hotel_rating_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_all_user_hotel_rating_by_hotel_id(self, hotel_id) -> UserRatingHotel:
        try:
            with session_scope() as db:
                user_hotel_rating_db = db.query(UserRatingHotel).filter(UserRatingHotel.hotel_id == hotel_id).all()
                if user_hotel_rating_db is None:
                    return None
                else:
                    return user_hotel_rating_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None


crud_user_hotel_rating = CRUDUserHotelRating()