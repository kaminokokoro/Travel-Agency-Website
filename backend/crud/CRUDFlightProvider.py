from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from backend.db.db import session_scope
from backend.db.model import FlightProvider, generate_uuid, UserRatingFlightProvider
from backend.util import schemas


class CRUDFlightProvider:

    def create_flight_provider(self, flight_provider: schemas.FlightProviderCreate) -> FlightProvider:
        """Create Flight Provider"""
        try:
            with session_scope() as db:
                flight_provider_db = FlightProvider(id=generate_uuid(),
                                                    name=flight_provider.name, phone_number=flight_provider.phone_number,
                                                    description=flight_provider.description, address=flight_provider.address)
                db.add(flight_provider_db)
                db.commit()
                db.refresh(flight_provider_db)
                return flight_provider_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def update_flight_provider(self, flight_provider: schemas.FlightProviderUpdate) -> FlightProvider:
        try:
            with session_scope() as db:
                flight_provider_db = db.query(FlightProvider).filter(FlightProvider.id == flight_provider.id).first()
                if flight_provider_db is None:
                    return None
                else:
                    flight_provider_db.name = flight_provider.name
                    flight_provider_db.phone_number = flight_provider.phone_number
                    flight_provider_db.description = flight_provider.description
                    flight_provider_db.address = flight_provider.address
                    db.commit()
                    db.refresh(flight_provider_db)
                    return flight_provider_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None



    def delete_flight_provider(self, flight_provider: schemas.FlightProviderDelete) -> FlightProvider:
        try:
            with session_scope() as db:
                flight_provider_db = db.query(FlightProvider).filter(FlightProvider.id == flight_provider.id).first()
                if flight_provider_db is None:
                    return None
                else:
                    db.delete(flight_provider_db)
                    db.commit()
                    return flight_provider_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_flight_provider(self, flight_provider_id) -> FlightProvider:
        try:
            with session_scope() as db:
                flight_provider_db = db.query(FlightProvider).filter(FlightProvider.id == flight_provider_id).first()
                return flight_provider_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_all_flight_providers_by_rating(self):
        try:
            with session_scope() as db:
                flight_providers = db.query(FlightProvider).outerjoin(UserRatingFlightProvider, FlightProvider.id == UserRatingFlightProvider.flight_provider_id).group_by(FlightProvider.id).order_by(func.avg(UserRatingFlightProvider.rating).desc()).all()
                return flight_providers
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None


crud_flight_provider = CRUDFlightProvider()