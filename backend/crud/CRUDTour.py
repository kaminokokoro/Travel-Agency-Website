from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from backend.db.db import session_scope
from backend.db.model import Tour, generate_uuid, UserRatingTour
from backend.util import schemas


class CRUDTour:

    def create_tour(self, tour: schemas.TourCreate) -> Tour:
        """Create Tour"""
        try:
            with session_scope() as db:
                tour_db = Tour(id=generate_uuid(),
                               name=tour.name, description=tour.description, duration=tour.duration,
                               departure=tour.departure, destination=tour.destination, adult_price=tour.adult_price,
                               child_price=tour.child_price
                               )
                db.add(tour_db)
                db.commit()
                db.refresh(tour_db)
                return tour_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def update_tour(self, tour: schemas.TourUpdate) -> Tour:
        try:
            with session_scope() as db:
                tour_db = db.query(Tour).filter(Tour.id == tour.id).first()
                if tour_db is None:
                    return None
                else:
                    tour_db.name = tour.name
                    tour_db.description = tour.description
                    tour_db.duration = tour.duration
                    tour_db.departure = tour.departure
                    tour_db.destination = tour.destination
                    tour_db.adult_price = tour.adult_price
                    tour_db.child_price = tour.child_price
                    db.commit()
                    db.refresh(tour_db)
                    return tour_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def delete_tour(self, tour: schemas.TourDelete) -> Tour:
        try:
            with session_scope() as db:
                tour_db = db.query(Tour).filter(Tour.id == tour.id).first()
                if tour_db is None:
                    return None
                else:
                    db.delete(tour_db)
                    db.commit()
                    return tour_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_tour(self, tour_id) -> Tour:
        try:
            with session_scope() as db:
                tour_db = db.query(Tour).filter(Tour.id == tour_id).first()
                return tour_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_all_tour_filter(self, page_number, page_size, destination, name):
        try:
            with session_scope() as db:
                if name is None:
                    name = ""
                if destination is None:
                    tour_db = db.query(Tour).filter(Tour.name.like(f"%{name}%")).limit(page_size).offset(
                        (page_number - 1) * page_size).all()
                else:
                    tour_db = db.query(Tour).filter(
                        and_(Tour.destination == destination, Tour.name.like(f"%{name}%"))).limit(page_size).offset(
                        (page_number - 1) * page_size).all()

                return tour_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None


crud_tour = CRUDTour()
