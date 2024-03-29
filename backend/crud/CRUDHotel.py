from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_, func, distinct
from sqlalchemy.orm import joinedload

from backend.db.db import session_scope
from backend.db.model import Hotel, generate_uuid, UserRatingHotel, HotelServices
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

    def get_hotel(self, hotel_id):
        try:
            with session_scope() as db:
                hotel_data = (
                    db.query(
                        Hotel,
                        func.avg(UserRatingHotel.rating).label('average_rating'),
                        func.count(distinct(UserRatingHotel.id)).label('rating_count'),
                        func.min(HotelServices.price).label('min_price')
                    )
                    .outerjoin(UserRatingHotel)
                    .outerjoin(HotelServices)
                    .filter(Hotel.id == hotel_id)
                    .group_by(Hotel.id)
                    .first()
                )

                if hotel_data is None:
                    return None
                else:
                    hotel, avg_rating, rating_count, min_price = hotel_data
                    hotel_dict = hotel.__dict__
                    hotel_dict['average_rating'] = avg_rating
                    hotel_dict['rating_count'] = rating_count
                    hotel_dict['min_price'] = min_price
                    return hotel_dict
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None

    def get_all_hotel(self, page_number: int, page_size: int):
        try:
            with session_scope() as db:
                hotels = (
                    db.query(
                        Hotel,
                        func.avg(UserRatingHotel.rating).label('average_rating'),
                        func.count(distinct(UserRatingHotel.id)).label('rating_count'),
                        func.min(HotelServices.price).label('min_price')  # Fetch minimum price
                    )
                    .outerjoin(UserRatingHotel)
                    .outerjoin(HotelServices)
                    .options(joinedload(Hotel.services))
                    .group_by(Hotel.id)
                    .order_by(func.avg(UserRatingHotel.rating).desc())
                    .limit(page_size)
                    .offset((page_number - 1) * page_size)
                    .all()
                )
                # Convert to list of dictionaries
                serialized_hotels = []
                for hotel, avg_rating, rating_count, min_price in hotels:
                    hotel_dict = hotel.__dict__
                    hotel_dict['average_rating'] = avg_rating
                    hotel_dict['rating_count'] = rating_count
                    hotel_dict['min_price'] = min_price
                    serialized_hotels.append(hotel_dict)

                return serialized_hotels
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None



    def get_hotel_filter(self, name_hotel, city_hotel, page_number: int, page_size: int):
        try:
            with session_scope() as db:
                query = (
                    db.query(
                        Hotel,
                        func.avg(UserRatingHotel.rating).label('average_rating'),
                        func.count(distinct(UserRatingHotel.id)).label('rating_count'),
                        func.min(HotelServices.price).label('min_price')
                    )
                    .outerjoin(UserRatingHotel)
                    .outerjoin(HotelServices)
                    .filter(Hotel.name.like(f"%{name_hotel}%"))
                )

                if city_hotel:
                    query = query.filter(Hotel.city == city_hotel)

                hotels = (
                    query.group_by(Hotel.id)
                    .order_by(func.avg(UserRatingHotel.rating).desc())
                    .limit(page_size)
                    .offset((page_number - 1) * page_size)
                    .all()
                )

                serialized_hotels = []
                for hotel, avg_rating, rating_count, min_price in hotels:
                    hotel_dict = hotel.__dict__
                    hotel_dict['average_rating'] = avg_rating
                    hotel_dict['rating_count'] = rating_count
                    hotel_dict['min_price'] = min_price
                    serialized_hotels.append(hotel_dict)

                return serialized_hotels
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return None


crud_hotel = CRUDHotel()

# crud_hotel.create_hotel(hotel=schemas.HotelCreate(name="hotel1", phone_number="123", description="123",address="123",
#                                                   city="123",state="123",zip_code="123"))
# # crud_hotel.create_hotel(hotel=schemas.HotelCreate(name="hotel2", phone_number="123", description="123"))
# print({"test":jsonable_encoder(crud_hotel.get_all_hotel(page_number=1, page_size=10))})
# crud_hotel.update_hotel(hotel=schemas.HotelUpdate(id="1",name="hotel1", phone_number="123", description="123"))
