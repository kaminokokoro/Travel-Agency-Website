from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_, func
from backend.db.db import session_scope
from backend.db.model import Hotel, generate_uuid, UserRatingHotel
from backend.util import schemas


# from backend.util.schemas import HotelGet, HotelCreate, HotelUpdate, HotelDelete

class CRUDHotel:
    def create_hotel(self, hotel: schemas.HotelCreate) -> Hotel:
        """Create Hotel"""
        try:
            with session_scope() as db:
                hotel_db = Hotel(id=generate_uuid(), name=hotel.name, phone_number=hotel.phone_number,
                                 description=hotel.description, address=hotel.address, city=hotel.city,
                                 state=hotel.state, zip_code=hotel.zip_code)
                db.add(hotel_db)
                db.commit()
                db.refresh(hotel_db)
                return hotel_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def update_hotel(self, hotel: schemas.HotelUpdate) -> Hotel:
        try:
            with session_scope() as db:
                hotel_db = db.query(Hotel).filter(Hotel.id == hotel.id).first()
                if hotel_db is None:
                    return None
                else:
                    hotel_db.name = hotel.name
                    hotel_db.phone_number = hotel.phone_number
                    hotel_db.description = hotel.description
                    hotel_db.address = hotel.address
                    hotel_db.city = hotel.city
                    hotel_db.state = hotel.state
                    hotel_db.zip_code = hotel.zip_code
                    db.commit()
                    db.refresh(hotel_db)
                    return hotel_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def delete_hotel(self, hotel: schemas.HotelDelete) -> Hotel:
        try:
            with session_scope() as db:
                hotel_db = db.query(Hotel).filter(Hotel.id == hotel.id).first()
                if hotel_db is None:
                    return None
                else:
                    db.delete(hotel_db)
                    db.commit()
                    return hotel_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_hotel(self, hotel_id) :
        try:
            with session_scope() as db:
                hotel_db = db.query(Hotel).filter(Hotel.id == hotel_id).first()
                if hotel_db is None:
                    return None
                else:
                    return hotel_db
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_all_hotel(self, page_number: int, page_size: int) :
        try:
            with session_scope() as db:
                hotels = (
                    db.query(Hotel, func.avg(UserRatingHotel.rating).label('average_rating'))
                    .join(UserRatingHotel)
                    .group_by(Hotel.id).order_by(func.avg(UserRatingHotel.rating).desc())
                    .limit(page_size)
                    .offset((page_number - 1) * page_size)
                    .all()
                )
                # Convert to list of dictionaries
                serialized_hotels = []
                for hotel, avg_rating in hotels:
                    hotel_dict = hotel.__dict__
                    hotel_dict['average_rating'] = avg_rating
                    serialized_hotels.append(hotel_dict)

                return serialized_hotels
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    # def get_hotel_filter(self,hotel_filter) -> Hotel:
    #     try:
    #         with session_scope() as db:
    #             hotels = db.query(Hotel).filter(and_(Hotel.name==hotel_filter.name,Hotel.city==hotel_filter.city)).all()
    #             return hotels
    #     except SQLAlchemyError as e:
    #         error = str(e.__dict__['orig'])
    #         print(error)
    #         return None


crud_hotel = CRUDHotel()

# crud_hotel.create_hotel(hotel=schemas.HotelCreate(name="hotel1", phone_number="123", description="123",address="123",
#                                                   city="123",state="123",zip_code="123"))
# # crud_hotel.create_hotel(hotel=schemas.HotelCreate(name="hotel2", phone_number="123", description="123"))
# print({"test":jsonable_encoder(crud_hotel.get_all_hotel(page_number=1, page_size=10))})
# crud_hotel.update_hotel(hotel=schemas.HotelUpdate(id="1",name="hotel1", phone_number="123", description="123"))