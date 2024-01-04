from sqlalchemy import func, and_
from sqlalchemy.exc import SQLAlchemyError
from backend.db.db import session_scope
from backend.db.model import TourDate, generate_uuid
from backend.util import schemas


class CRUDTourDate:

    def create_tour_date(self, tour_date: schemas.TourDateCreate) -> TourDate:
        """Create Tour Date"""
        try:
            with session_scope() as db:
                tour_date_db = TourDate(id=generate_uuid(),
                                        tour_id=tour_date.tour_id, departure_datetime=tour_date.departure_datetime,
                                        return_datetime=tour_date.return_datetime)
                db.add(tour_date_db)
                db.commit()
                db.refresh(tour_date_db)
                return tour_date_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def update_tour_date(self, tour_date: schemas.TourDateUpdate) -> TourDate:
        try:
            with session_scope() as db:
                tour_date_db = db.query(TourDate).filter(TourDate.id == tour_date.id).first()
                if tour_date_db is None:
                    return None
                else:
                    tour_date_db.tour_id = tour_date.tour_id
                    tour_date_db.departure_datetime = tour_date.departure_datetime
                    tour_date_db.return_datetime = tour_date.return_datetime
                    db.commit()
                    db.refresh(tour_date_db)
                    return tour_date_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def delete_tour_date(self, tour_date: schemas.TourDateDelete) -> TourDate:
        try:
            with session_scope() as db:
                tour_date_db = db.query(TourDate).filter(TourDate.id == tour_date.id).first()
                if tour_date_db is None:
                    return None
                else:
                    db.delete(tour_date_db)
                    db.commit()
                    return tour_date_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_tour_date_by_id(self, tour_date_id) -> TourDate:
        try:
            with session_scope() as db:
                tour_date_db = db.query(TourDate).filter(TourDate.id == tour_date_id).first()
                if tour_date_db is None:
                    return None
                else:
                    return tour_date_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_tour_date_from_now_by_tour_id(self, tour_id) -> TourDate:
        try:
            with session_scope() as db:
                datetime_now = func.now()
                tour_date_db = db.query(TourDate).filter(
                    and_(TourDate.tour_id == tour_id, TourDate.departure_datetime >= datetime_now)).all()
                if tour_date_db is None:
                    return None
                else:
                    return tour_date_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_tour_date_by_tour_id(self, tour_id, page_num, page_size) -> TourDate:
        try:
            with session_scope() as db:
                tour_date_db = db.query(TourDate).filter(TourDate.tour_id == tour_id).offset((page_num - 1) * page_size).limit(page_size).all()
                if tour_date_db is None:
                    return None
                else:
                    return tour_date_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None


crud_tour_date = CRUDTourDate()
