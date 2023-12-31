from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from backend.db.db import session_scope
from backend.db.model import HotelServices, generate_uuid, Hotel, UserRatingHotel
from backend.util import schemas


class CRUDHotelService:
    def create_hotel_service(self, hotel_service: schemas.HotelServiceCreate) -> HotelServices:
        """Create Hotel Service"""
        try:
            with session_scope() as db:
                hotel_service_db = HotelServices(id=generate_uuid(), hotel_id=hotel_service.hotel_id)
                hotel_service_db.name = hotel_service.name
                hotel_service_db.room_capacity = hotel_service.room_capacity
                hotel_service_db.room_type = hotel_service.room_type
                hotel_service_db.price = hotel_service.price
                hotel_service_db.description = hotel_service.description
                # hotel_service_db.image = hotel_service.image
                db.add(hotel_service_db)
                db.commit()
                db.refresh(hotel_service_db)
                return hotel_service_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def update_hotel_service(self, hotel_service: schemas.HotelServiceUpdate) -> HotelServices:
        try:
            with session_scope() as db:
                hotel_service_db = db.query(HotelServices).filter(HotelServices.id == hotel_service.id).first()
                if hotel_service_db is None:
                    return None
                else:
                    hotel_service_db.hotel_id = hotel_service.hotel_id
                    hotel_service_db.name = hotel_service.name
                    hotel_service_db.room_capacity = hotel_service.room_capacity
                    hotel_service_db.room_type = hotel_service.room_type
                    hotel_service_db.price = hotel_service.price
                    hotel_service_db.description = hotel_service.description
                    db.commit()
                    db.refresh(hotel_service_db)
                    return hotel_service_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def delete_hotel_service(self, hotel_service: schemas.HotelServiceDelete) -> HotelServices:
        try:
            with session_scope() as db:
                hotel_service_db = db.query(HotelServices).filter(HotelServices.id == hotel_service.id).first()
                if hotel_service_db is None:
                    return None
                else:
                    db.delete(hotel_service_db)
                    db.commit()
                    return hotel_service_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_hotel_service(self, hotel_service_id) -> HotelServices:
        try:
            with session_scope() as db:
                hotel_service_db = db.query(HotelServices).filter(and_(HotelServices.id == hotel_service_id)).first()
                return hotel_service_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    # def get_all_hotel_service(self, page_number: int = 1, page_size: int = 10) -> HotelServices:
    #     try:
    #         with session_scope() as db:
    #             hotel_service_db = db.query(HotelServices).join(Hotel).filter(and_(
    #                 HotelServices.hotel_id == Hotel.id)).join(UserRating).filter(and_(Hotel.id == UserRating.hotel_id)).limit(page_size).offset((page_number - 1) * page_size).all()
    #             # hotel_service_db = db.query(HotelServices).offset((page_number - 1) * page_size).limit(page_size).all()
    #             return hotel_service_db
    #     except SQLAlchemyError as e:
    #         error = str(e.__dict__['orig'])
    #         print(error)
    #         return None

    def get_all_hotel_service_by_hotel_id(self, hotel_id: str, page_number: int = 1, page_size: int = 10) -> HotelServices:
        try:
            with session_scope() as db:
                hotel_service_db = db.query(HotelServices).filter(
                    and_(HotelServices.hotel_id == hotel_id)).limit(page_size).offset(
                    (page_number - 1) * page_size).all()
                return hotel_service_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_hotel_service_filter(self, name_hotel, city_hotel, page_number: int = 1,
                                 page_size: int = 10) :
        try:
            with session_scope() as db:
                if name_hotel is None:
                    name_hotel = ""
                if city_hotel is None:
                    hotel_service_db = db.query(HotelServices).join(Hotel).filter(
                        Hotel.name.like(f"%{name_hotel}%")).limit(page_size).offset(
                        (page_number - 1) * page_size).all()
                else:
                    hotel_service_db = db.query(HotelServices).join(Hotel).filter(
                        and_(Hotel.name.like(f"%{name_hotel}%"),
                             Hotel.city == city_hotel)
                    ).limit(page_size).offset((page_number - 1) * page_size).all()

                # hotel_db= db.query(Hotel).filter(
                #     and_(Hotel.name.like(f"%{name_hotel}%"),
                #          Hotel.city == city_hotel)
                # ).limit(page_size).offset((page_number - 1) * page_size).all()
                return hotel_service_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None


crud_hotel_service = CRUDHotelService()
