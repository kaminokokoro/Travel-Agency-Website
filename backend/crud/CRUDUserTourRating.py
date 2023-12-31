from sqlalchemy.exc import SQLAlchemyError
from backend.db.db import session_scope
from backend.db.model import UserRatingTour, generate_uuid
from backend.util import schemas


class CRUDUserTourRating:

            def create_user_tour_rating(self, user_tour_rating: schemas.UserTourRatingCreate) -> UserRatingTour:
                """Create User Tour Rating"""
                try:
                    with session_scope() as db:
                        user_tour_rating_db = UserRatingTour(id=generate_uuid(),
                                                        user_id=user_tour_rating.user_id, tour_id=user_tour_rating.tour_id,
                                                        rating=user_tour_rating.rating, comment=user_tour_rating.comment)
                        db.add(user_tour_rating_db)
                        db.commit()
                        db.refresh(user_tour_rating_db)
                        return user_tour_rating_db
                except SQLAlchemyError as e:
                    error = str(e.__dict__['orig'])
                    print(error)
                    return None

            def update_user_tour_rating(self, user_tour_rating: schemas.UserTourRatingUpdate) -> UserRatingTour:
                try:
                    with session_scope() as db:
                        user_tour_rating_db = db.query(UserRatingTour).filter(UserRatingTour.id == user_tour_rating.id).first()
                        if user_tour_rating_db is None:
                            return None
                        else:
                            user_tour_rating_db.user_id = user_tour_rating.user_id
                            user_tour_rating_db.tour_id = user_tour_rating.tour_id
                            user_tour_rating_db.rating = user_tour_rating.rating
                            user_tour_rating_db.comment = user_tour_rating.comment
                            db.commit()
                            db.refresh(user_tour_rating_db)
                            return user_tour_rating_db
                except SQLAlchemyError as e:
                    error = str(e.__dict__['orig'])
                    print(error)
                    return None

            def delete_user_tour_rating(self, user_tour_rating: schemas.UserTourRatingDelete) -> UserRatingTour:
                try:
                    with session_scope() as db:
                        user_tour_rating_db = db.query(UserRatingTour).filter(UserRatingTour.id == user_tour_rating.id).first()
                        if user_tour_rating_db is None:
                            return None
                        else:
                            db.delete(user_tour_rating_db)
                            db.commit()
                            return user_tour_rating_db
                except SQLAlchemyError as e:
                    error = str(e.__dict__['orig'])
                    print(error)
                    return None

            def get_user_tour_rating(self, user_tour_rating_id) -> UserRatingTour:
                try:
                    with session_scope() as db:
                        user_tour_rating_db = db.query(UserRatingTour).filter(UserRatingTour.id == user_tour_rating_id).first()
                        return user_tour_rating_db
                except SQLAlchemyError as e:
                    error = str(e.__dict__['orig'])
                    print(error)
                    return None

            def get_user_tour_rating_by_user_id(self, user_id) -> UserRatingTour:
                try:
                    with session_scope() as db:
                        user_tour_rating_db = db.query(UserRatingTour).filter(UserRatingTour.user_id == user_id).all()
                        if user_tour_rating_db is None:
                            return None
                        else:
                            return user_tour_rating_db
                except SQLAlchemyError as e:
                    error = str(e.__dict__['orig'])
                    print(error)
                    return None

            def get_user_tour_rating_by_tour_id(self, tour_id) -> UserRatingTour:
                try:
                    with session_scope() as db:
                        user_tour_rating_db = db.query(UserRatingTour).filter(UserRatingTour.tour_id == tour_id).all()
                        if user_tour_rating_db is None:
                            return None
                        else:
                            return user_tour_rating_db
                except SQLAlchemyError as e:
                    error = str(e.__dict__['orig'])
                    print(error)
                    return None


crud_user_tour_rating = CRUDUserTourRating()