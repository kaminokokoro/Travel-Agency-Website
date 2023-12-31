from sqlalchemy.exc import SQLAlchemyError
from backend.db.db import session_scope
from backend.db.model import UserRatingFlightProvider, generate_uuid
from backend.util import schemas


class CRUDUserFlightProviderRating:

        def create_user_flight_provider_rating(self, user_flight_provider_rating: schemas.UserFlightProviderRatingCreate) -> UserRatingFlightProvider:
            """Create User Flight Provider Rating"""
            try:
                with session_scope() as db:
                    user_flight_provider_rating_db = UserRatingFlightProvider(id=generate_uuid(),
                                                    user_id=user_flight_provider_rating.user_id, flight_provider_id=user_flight_provider_rating.flight_provider_id,
                                                    rating=user_flight_provider_rating.rating, comment=user_flight_provider_rating.comment)
                    db.add(user_flight_provider_rating_db)
                    db.commit()
                    db.refresh(user_flight_provider_rating_db)
                    return user_flight_provider_rating_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def update_user_flight_provider_rating(self, user_flight_provider_rating: schemas.UserFlightProviderRatingUpdate) -> UserRatingFlightProvider:
            try:
                with session_scope() as db:
                    user_flight_provider_rating_db = db.query(UserRatingFlightProvider).filter(UserRatingFlightProvider.id == user_flight_provider_rating.id).first()
                    if user_flight_provider_rating_db is None:
                        return None
                    else:
                        user_flight_provider_rating_db.user_id = user_flight_provider_rating.user_id
                        user_flight_provider_rating_db.flight_provider_id = user_flight_provider_rating.flight_provider_id
                        user_flight_provider_rating_db.rating = user_flight_provider_rating.rating
                        user_flight_provider_rating_db.comment = user_flight_provider_rating.comment
                        db.commit()
                        db.refresh(user_flight_provider_rating_db)
                        return user_flight_provider_rating_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def delete_user_flight_provider_rating(self, user_flight_provider_rating: schemas.UserFlightProviderRatingDelete) -> UserRatingFlightProvider:
            try:
                with session_scope() as db:
                    user_flight_provider_rating_db = db.query(UserRatingFlightProvider).filter(UserRatingFlightProvider.id == user_flight_provider_rating.id).first()
                    if user_flight_provider_rating_db is None:
                        return None
                    else:
                        db.delete(user_flight_provider_rating_db)
                        db.commit()
                        return user_flight_provider_rating_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def get_user_flight_provider_rating(self, user_flight_provider_rating_id) -> UserRatingFlightProvider:
            try:
                with session_scope() as db:
                    user_flight_provider_rating_db = db.query(UserRatingFlightProvider).filter(UserRatingFlightProvider.id == user_flight_provider_rating_id).first()
                    return user_flight_provider_rating_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def get_user_flight_provider_rating_by_user_id(self, user_id) -> UserRatingFlightProvider:
            try:
                with session_scope() as db:
                    user_flight_provider_rating_db = db.query(UserRatingFlightProvider).filter(UserRatingFlightProvider.user_id == user_id).all()
                    return user_flight_provider_rating_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None

        def get_user_flight_provider_rating_by_flight_provider_id(self, flight_provider_id) -> UserRatingFlightProvider:
            try:
                with session_scope() as db:
                    user_flight_provider_rating_db = db.query(UserRatingFlightProvider).filter(UserRatingFlightProvider.flight_provider_id == flight_provider_id).all()
                    return user_flight_provider_rating_db
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return None



crud_user_flight_provider_rating = CRUDUserFlightProviderRating()

