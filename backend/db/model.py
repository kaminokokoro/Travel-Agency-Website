from sqlalchemy import Column, Integer, String, Boolean, SmallInteger, DateTime, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid
Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())
class User(Base):
    __tablename__ = "user_account"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    phone_number = Column(String(20), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    authorization = Column(SmallInteger)
    profile = relationship("UserProfile", back_populates="user",cascade="all, delete-orphan")
    # login_attempt = relationship("UserLoginAttempt",  back_populates="user")
    card = relationship("UserCard", back_populates="user",cascade="all, delete-orphan")
    # saved = relationship("UserSaved", back_populates="user")
    # rating = relationship("UserRating", back_populates="user",cascade="all, delete-orphan")
    user_rating_hotel = relationship("UserRatingHotel", back_populates="user",cascade="all, delete-orphan")
    user_rating_tour = relationship("UserRatingTour", back_populates="user",cascade="all, delete-orphan")
    user_rating_flight = relationship("UserRatingFlightProvider", back_populates="user",cascade="all, delete-orphan")
    # payment = relationship("Payment", back_populates="user",cascade="all, delete-orphan")
    tour_booking = relationship("TourBooking", back_populates="user",cascade="all, delete-orphan")
    hotel_booking = relationship("HotelBooking", back_populates="user",cascade="all, delete-orphan")
    flight_booking = relationship("FlightBooking", back_populates="user",cascade="all, delete-orphan")
    # created_at = Column(DateTime)
    # updated_at = Column(DateTime)
    # deleted_at = Column(DateTime)
    # created_by = Column(Integer)
    # updated_by = Column(Integer)
    # deleted_by = Column(Integer)

    def __repr__(self) -> str:
        return f"User(id={self.id!r})"

class UserProfile(Base):
    __tablename__ = "user_profile"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender: Boolean = Column(Boolean, nullable=False)
    email = Column(String(200))
    street= Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(50))
    # profile_image = Column(String(200))
    date_of_birth = Column(Date)
    user_id = Column(String(36), ForeignKey('user_account.id'), unique=True)
    user = relationship("User", back_populates="profile")

# class UserLoginAttempt(Base):
#     __tablename__ = "user_login_attempt"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     user_id = Column(String(36), ForeignKey('user_account.id'), unique=True)
#     user = relationship("User", back_populates="login_attempt")
#     login_attempt = Column(Integer)
#     last_login_attempt = Column(DateTime)

class UserCard(Base):
    __tablename__ = "user_card"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    user_id = Column(String(36), ForeignKey('user_account.id'),nullable=False)
    user = relationship("User", back_populates="card")
    card_number = Column(String(20),nullable=False, unique=True)
    name_on_card = Column(String(50), nullable=False)
    cvv = Column(String(10), nullable=False)
    expiry_date = Column(Date, nullable=False)
    hotel_booking = relationship("HotelBooking", back_populates="user_card",cascade="all, delete-orphan")
    tour_booking = relationship("TourBooking", back_populates="user_card",cascade="all, delete-orphan")
    flight_booking = relationship("FlightBooking", back_populates="user_card",cascade="all, delete-orphan")

# class UserSaved(Base):
#     __tablename__ = "user_saved"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     user_id = Column(String(36), ForeignKey('user_account.id'))
#     user = relationship("User", back_populates="saved")
#     tour_id = Column(String(36), ForeignKey('tour.id'))
#     tour = relationship("Tour", back_populates="saved")

class UserRatingHotel(Base):
    __tablename__ = "user_rating_hotel"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    user_id = Column(String(36), ForeignKey('user_account.id'),)
    # user = relationship("User", back_populates="rating")
    user = relationship("User", back_populates="user_rating_hotel")
    hotel_id = Column(String(36), ForeignKey('hotel.id'))
    hotel = relationship("Hotel", back_populates="rating")
    rating = Column(Integer)
    comment = Column(String(200))

class UserRatingTour(Base):
    __tablename__ = "user_rating_tour"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    user_id = Column(String(36), ForeignKey('user_account.id'))
    # user = relationship("User", back_populates="rating")
    user = relationship("User", back_populates="user_rating_tour")
    tour_id = Column(String(36), ForeignKey('tour.id'))
    tour = relationship("Tour", back_populates="rating")
    rating = Column(Integer)
    comment = Column(String(200))

class UserRatingFlightProvider(Base):
    __tablename__ = "user_rating_flight_provider"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    user_id = Column(String(36), ForeignKey('user_account.id'))
    # user = relationship("User", back_populates="rating")
    user = relationship("User", back_populates="user_rating_flight")
    flight_provider_id = Column(String(36), ForeignKey('flight_provider.id'))
    flight_provider = relationship("FlightProvider", back_populates="rating")
    rating = Column(Integer)
    comment = Column(String(200))

class Tour(Base):
    __tablename__ = "tour"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    name = Column(String(500), nullable=False)
    destination = Column(String(200), nullable=False)
    # high_lights = Column(String(200))
    duration = Column(String(50), nullable=False)
    # Service_available_in = Column(String(50))
    description = Column(String(10000))
    # experience= Column(String(200))
    adult_price = Column(Integer)
    child_price = Column(Integer)
    # departure_from = Column(String(200))
    # location = Column(String(200))
    # location_link = Column(String(200))
    # phone_number = Column(String(20))
    # transport_description = Column(String(200))
    rating = relationship("UserRatingTour", back_populates="tour",cascade="all, delete-orphan")
    tour_date = relationship("TourDate", back_populates="tour",cascade="all, delete-orphan")

    # user_id = Column(String(36), ForeignKey('user_account.id'), unique=True)
    # user_s = relationship("User", back_populates="tour")
    # saved = relationship("UserSaved", back_populates="tour")
    # created_at = Column(DateTime)
    # updated_at = Column(DateTime)
    # deleted_at = Column(DateTime)
    # created_by = Column(Integer)
    # updated_by = Column(Integer)
    # deleted_by = Column(Integer)

class TourDate(Base):
    __tablename__ = "tour_date"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    tour_id = Column(String(36), ForeignKey('tour.id'))
    tour = relationship("Tour", back_populates="tour_date")
    # max_people = Column(Integer)
    departure_datetime = Column(Date)
    return_datetime = Column(Date)
    tour_booking = relationship("TourBooking", back_populates="tour_date",cascade="all, delete-orphan")

# class TourItinerary(Base):
#     __tablename__ = "tour_itinerary"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     tour_id = Column(String(36), ForeignKey('tour.id'), unique=True)
#     tour = relationship("Tour", back_populates="tour_itinerary",cascade="all, delete-orphan")
#     day = Column(Integer)
#     title = Column(String(50))
#     description = Column(String(200))

class TourBooking(Base):
    __tablename__ = "tour_booking"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    user_id = Column(String(36), ForeignKey('user_account.id'))
    user = relationship("User", back_populates="tour_booking")
    user_card_id = Column(String(36), ForeignKey('user_card.id'))
    user_card = relationship("UserCard", back_populates="tour_booking")
    tour_date_id = Column(String(36), ForeignKey('tour_date.id'))
    tour_date = relationship("TourDate", back_populates="tour_booking")
    number_of_adult = Column(Integer, nullable=False, default=1)
    number_of_child = Column(Integer, nullable=False, default=0)
    payment_status = Column(SmallInteger)
    payment_time = Column(DateTime)
    payment_description = Column(String(200))

# class Payment(Base):
#     __tablename__ = "payment"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     user_id = Column(String(36), ForeignKey('user_account.id'))
#     user = relationship("User", back_populates="payment")
#     hotel_booking = relationship("HotelBooking", back_populates="payment")
#     tour_booking = relationship("TourBooking", back_populates="payment")
#     flight_booking = relationship("FlightBooking", back_populates="payment")
#     payment_method = Column(String(50))
#     payment_status = Column(SmallInteger)
#     payment_time = Column(DateTime)
#     payment_description = Column(String(200))


class HotelBooking(Base):
    __tablename__ = "hotel_booking"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    user_id = Column(String(36), ForeignKey('user_account.id'))
    user = relationship("User", back_populates="hotel_booking")
    user_card_id = Column(String(36), ForeignKey('user_card.id'))
    user_card = relationship("UserCard", back_populates="hotel_booking")
    hotel_services_id = Column(String(36), ForeignKey('hotel_services.id'))
    hotel_services = relationship("HotelServices", back_populates="hotel_booking")
    number_of_room= Column(Integer, nullable=False, default=1)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    payment_status = Column(SmallInteger)
    payment_time = Column(DateTime)
    payment_description = Column(String(200))

class HotelServices(Base):
    __tablename__ = "hotel_services"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    name = Column(String(50), nullable=False)
    room_type = Column(String(50), nullable=False)
    room_capacity = Column(Integer, nullable=False)
    description = Column(String(2000))
    price = Column(Integer, nullable=False)
    hotel_id = Column(String(36), ForeignKey('hotel.id'))
    hotel = relationship("Hotel", back_populates="services")
    hotel_booking = relationship("HotelBooking", back_populates="hotel_services",cascade="all, delete-orphan")
    # created_at = Column(DateTime)
    # updated_at = Column(DateTime)
    # deleted_at = Column(DateTime)
    # created_by = Column(Integer)
    # updated_by = Column(Integer)
    # deleted_by = Column(Integer)

class Hotel(Base):
    __tablename__ = "hotel"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(20))
    description = Column(String(2000))
    address = Column(String(200))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(50))
    services = relationship("HotelServices", back_populates="hotel",cascade="all, delete-orphan")
    rating = relationship("UserRatingHotel", back_populates="hotel",cascade="all, delete-orphan")
    # rating = relationship("", back_populates="hotel")
    # created_at = Column(DateTime)
    # updated_at = Column(DateTime)
    # deleted_at = Column(DateTime)
    # created_by = Column(Integer)
    # updated_by = Column(Integer)
    # deleted_by = Column(Integer)

class FlightProvider(Base):
    __tablename__ = "flight_provider"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    name = Column(String(50), nullable=False)
    description = Column(String(2000))
    email = Column(String(200))
    phone_number = Column(String(20))
    flight = relationship("Flight", back_populates="flight_provider",cascade="all, delete-orphan")
    rating = relationship("UserRatingFlightProvider", back_populates="flight_provider",cascade="all, delete-orphan")

class Flight(Base):
    __tablename__ = "flight"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    name = Column(String(50), nullable=False)
    description = Column(String(2000))
    departure_from = Column(String(200))
    arrival_to = Column(String(200))
    departure_date = Column(DateTime)
    arrival_date= Column(DateTime)
    flight_ticket = relationship("FlightTicket", back_populates="flight",cascade="all, delete-orphan")
    flight_provider_id = Column(String(36), ForeignKey('flight_provider.id'))
    flight_provider = relationship("FlightProvider", back_populates="flight")

    # created_at = Column(DateTime)
    # updated_at = Column(DateTime)
    # deleted_at = Column(DateTime)
    # created_by = Column(Integer)
    # updated_by = Column(Integer)
    # deleted_by = Column(Integer)

class FlightTicket(Base):
    __tablename__ = "flight_ticket"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    name = Column(String(50), nullable=False)
    description = Column(String(2000))
    seat_class = Column(String(50), nullable=False)
    adult_price = Column(Integer)
    child_price = Column(Integer)
    baby_price = Column(Integer)
    flight_id = Column(String(36), ForeignKey('flight.id'))
    flight = relationship("Flight", back_populates="flight_ticket")
    flight_booking = relationship("FlightBooking", back_populates="departure_flight_ticket",cascade="all, delete-orphan")

    # created_at = Column(DateTime)
    # updated_at = Column(DateTime)
    # deleted_at = Column(DateTime)
    # created_by = Column(Integer)
    # updated_by = Column(Integer)
    # deleted_by = Column(Integer)

class FlightBooking(Base):
    __tablename__ = "flight_booking"
    id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
    user_id = Column(String(36), ForeignKey('user_account.id'))
    user = relationship("User", back_populates="flight_booking")
    user_card_id = Column(String(36), ForeignKey('user_card.id'))
    user_card = relationship("UserCard", back_populates="flight_booking")
    departure_flight_ticket_id = Column(String(36), ForeignKey('flight_ticket.id'))
    departure_flight_ticket = relationship("FlightTicket", back_populates="flight_booking")
    return_flight_ticket_id = Column(String(36))
    # return_flight_ticket = relationship("FlightTicket", back_populates="flight_booking")
    number_of_adult = Column(Integer,default=0)
    number_of_child = Column(Integer, default=0)
    number_of_baby = Column(Integer, default=0)
    payment_status = Column(SmallInteger)
    payment_time = Column(DateTime)
    payment_description = Column(String(200))


# class HotelProvider(Base):
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     name = Column(String(50), nullable=False)
#     description = Column(String(200))
#     email = Column(String(200))
#     phone_number = Column(String(20))
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     deleted_at = Column(DateTime)
#     created_by = Column(Integer)
#     updated_by = Column(Integer)
#     deleted_by = Column(Integer)

# class HotelBooking(Base):
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     user_id = Column(Integer, ForeignKey('user.id'), unique=True)
#     user = relationship("User", back_populates="hotel_booking")
#     hotel_id = Column(Integer, ForeignKey('hotel.id'), unique=True)
#     hotel = relationship("Hotel", back_populates="hotel_booking")
#     check_in = Column(DateTime)
#     check_out = Column(DateTime)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     deleted_at = Column(DateTime)
#     created_by = Column(Integer)
#     updated_by = Column(Integer)
#     deleted_by = Column(Integer)




# class Account(Base):
#     __tablename__ = "account"
#     id = Column(Integer, primary_key=True, default=uuid.uuid4, unique=True)
#     username = Column(String(30), nullable=False)


    # user_id = Column(Integer, ForeignKey("user_info.id"), unique=True,nullable=False)
    #
    # user_info = relationship("User", back_populates="id_account")

# class UsersLoginAttempt(Base):
#     __tablename__ = "users_login_attempt"
#     id = Column(Integer, primary_key=True, default=uuid.uuid4, unique=True)
#     user_id = Column(Integer, ForeignKey("user_info.id"), unique=True,nullable=False)
#     login_attempt = Column(Integer, nullable=False)
#     last_login_attempt = Column(DateTime, nullable=False)
#     user_info = relationship("User", back_populates="id_account")















# from sqlalchemy import Column, Integer, String, Boolean, SmallInteger, DateTime, ForeignKey, Table
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# import uuid
# Base = declarative_base()
#
# def generate_uuid():
#     return str(uuid.uuid4())
# class User(Base):
#     __tablename__ = "user_account"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     phone_number = Column(String(20), nullable=False, unique=True)
#     password = Column(String(200), nullable=False)
#     authorization = Column(SmallInteger)
#     profile = relationship("UserProfile", back_populates="user")
#     # login_attempt = relationship("UserLoginAttempt",  back_populates="user")
#     card = relationship("UserCard", back_populates="user")
#     # saved = relationship("UserSaved", back_populates="user")
#     rating = relationship("UserRating", back_populates="user")
#     payment = relationship("Payment", back_populates="user")
#
#     # created_at = Column(DateTime)
#     # updated_at = Column(DateTime)
#     # deleted_at = Column(DateTime)
#     # created_by = Column(Integer)
#     # updated_by = Column(Integer)
#     # deleted_by = Column(Integer)
#
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, fullname={self.fullname!r})"
#
# class UserProfile(Base):
#     __tablename__ = "user_profile"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     fullname = Column(String(50), nullable=False)
#     gender: Boolean = Column(Boolean, nullable=False)
#     email = Column(String(200))
#     street= Column(String(50))
#     city = Column(String(50))
#     state = Column(String(50))
#     zip_code = Column(String(50))
#     # profile_image = Column(String(200))
#     date_of_birth = Column(DateTime)
#     user_id = Column(String(36), ForeignKey('user_account.id'), unique=True)
#     user = relationship("User", back_populates="profile")
#
# # class UserLoginAttempt(Base):
# #     __tablename__ = "user_login_attempt"
# #     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
# #     user_id = Column(String(36), ForeignKey('user_account.id'), unique=True)
# #     user = relationship("User", back_populates="login_attempt")
# #     login_attempt = Column(Integer)
# #     last_login_attempt = Column(DateTime)
#
# class UserCard(Base):
#     __tablename__ = "user_card"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     user_id = Column(String(36), ForeignKey('user_account.id'), unique=True)
#     user = relationship("User", back_populates="card")
#     card_number = Column(String(20),nullable=False)
#     card_name = Column(String(50), nullable=False)
#     card_cvv = Column(String(10), nullable=False)
#     card_expire = Column(DateTime, nullable=False)
#
# # class UserSaved(Base):
# #     __tablename__ = "user_saved"
# #     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
# #     user_id = Column(String(36), ForeignKey('user_account.id'))
# #     user = relationship("User", back_populates="saved")
# #     tour_id = Column(String(36), ForeignKey('tour.id'))
# #     tour = relationship("Tour", back_populates="saved")
#
# class UserRating(Base):
#     __tablename__ = "user_rating"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     user_id = Column(String(36), ForeignKey('user_account.id'), unique=True)
#     user = relationship("User", back_populates="rating")
#     tour_id = Column(String(36), ForeignKey('tour.id'), unique=True)
#     tour = relationship("Tour", back_populates="rating")
#     hotel_id = Column(String(36), ForeignKey('hotel.id'), unique=True)
#     hotel = relationship("Hotel", back_populates="rating")
#     rating = Column(Integer)
#     comment = Column(String(200))
#
# class Tour(Base):
#     __tablename__ = "tour"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     name = Column(String(50), nullable=False)
#     destination = Column(String(200), nullable=False)
#     # high_lights = Column(String(200))
#     Duration = Column(String(50), nullable=False)
#     # Service_available_in = Column(String(50))
#     description = Column(String(5000))
#     # experience= Column(String(200))
#     price_adult = Column(Integer)
#     price_child = Column(Integer)
#     # departure_from = Column(String(200))
#     # location = Column(String(200))
#     # location_link = Column(String(200))
#     # phone_number = Column(String(20))
#     # transport_description = Column(String(200))
#     rating = relationship("UserRating", back_populates="tour",cascade="all, delete-orphan")
#     tour_date = relationship("TourDate", back_populates="tour",cascade="all, delete-orphan")
#
#     # user_id = Column(String(36), ForeignKey('user_account.id'), unique=True)
#     # user_s = relationship("User", back_populates="tour")
#     # saved = relationship("UserSaved", back_populates="tour")
#     # created_at = Column(DateTime)
#     # updated_at = Column(DateTime)
#     # deleted_at = Column(DateTime)
#     # created_by = Column(Integer)
#     # updated_by = Column(Integer)
#     # deleted_by = Column(Integer)
#
# class TourDate(Base):
#     __tablename__ = "tour_date"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     tour_id = Column(String(36), ForeignKey('tour.id'), unique=True)
#     tour = relationship("Tour", back_populates="tour_date")
#     # max_people = Column(Integer)
#     departure_date = Column(DateTime)
#     return_date = Column(DateTime)
#     tour_booking = relationship("TourBooking", back_populates="tour_date",cascade="all, delete-orphan")
#
# # class TourItinerary(Base):
# #     __tablename__ = "tour_itinerary"
# #     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
# #     tour_id = Column(String(36), ForeignKey('tour.id'), unique=True)
# #     tour = relationship("Tour", back_populates="tour_itinerary",cascade="all, delete-orphan")
# #     day = Column(Integer)
# #     title = Column(String(50))
# #     description = Column(String(200))
#
# class TourBooking(Base):
#     __tablename__ = "tour_booking"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     payment_id = Column(String(36), ForeignKey('payment.id'), unique=True)
#     payment = relationship("Payment", back_populates="tour_booking")
#     tour_date_id = Column(String(36), ForeignKey('tour_date.id'), unique=True)
#     tour_date = relationship("TourDate", back_populates="tour_booking")
#     number_adult = Column(Integer, nullable=False, default=1)
#     number_child = Column(Integer, nullable=False, default=0)
#
# class Payment(Base):
#     __tablename__ = "payment"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     user_id = Column(String(36), ForeignKey('user_account.id'), unique=True)
#     user = relationship("User", back_populates="payment")
#     hotel_booking = relationship("HotelBooking", back_populates="payment")
#     tour_booking = relationship("TourBooking", back_populates="payment")
#     flight_booking = relationship("FlightBooking", back_populates="payment")
#     payment_method = Column(String(50))
#     payment_status = Column(String(50))
#     payment_date = Column(DateTime)
#     payment_amount = Column(Integer)
#     payment_currency = Column(String(50))
#     payment_description = Column(String(200))
#     # created_at = Column(DateTime)
#     # updated_at = Column(DateTime)
#     # deleted_at = Column(DateTime)
#     # created_by = Column(Integer)
#     # updated_by = Column(Integer)
#     # deleted_by = Column(Integer)
#
#
# class HotelBooking(Base):
#     __tablename__ = "hotel_booking"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     payment_id = Column(String(36), ForeignKey('payment.id'), unique=True)
#     payment = relationship("Payment", back_populates="hotel_booking")
#     hotel_services_id = Column(String(36), ForeignKey('hotel_services.id'), unique=True)
#     hotel_services = relationship("HotelServices", back_populates="hotel_booking")
#     numbers_of_room = Column(Integer, nullable=False, default=1)
#     check_in = Column(DateTime, nullable=False)
#     check_out = Column(DateTime, nullable=False)
#
# class HotelServices(Base):
#     __tablename__ = "hotel_services"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     name = Column(String(50), nullable=False)
#     description = Column(String(200))
#     room_capacity = Column(Integer, nullable=False)
#     price = Column(Integer, nullable=False)
#     hotel_id = Column(String(36), ForeignKey('hotel.id'), unique=True)
#     hotel = relationship("Hotel", back_populates="services")
#     hotel_booking = relationship("HotelBooking", back_populates="hotel_services")
#     # created_at = Column(DateTime)
#     # updated_at = Column(DateTime)
#     # deleted_at = Column(DateTime)
#     # created_by = Column(Integer)
#     # updated_by = Column(Integer)
#     # deleted_by = Column(Integer)
#
# class Hotel(Base):
#     __tablename__ = "hotel"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     name = Column(String(50), nullable=False)
#     phone_number = Column(String(20))
#     description = Column(String(2000))
#     address = Column(String(200))
#     city = Column(String(50))
#     services = relationship("HotelServices", back_populates="hotel")
#     rating = relationship("UserRating", back_populates="hotel")
#     # created_at = Column(DateTime)
#     # updated_at = Column(DateTime)
#     # deleted_at = Column(DateTime)
#     # created_by = Column(Integer)
#     # updated_by = Column(Integer)
#     # deleted_by = Column(Integer)
#
# class FlightProvider(Base):
#     __tablename__ = "flight_provider"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     name = Column(String(50), nullable=False)
#     description = Column(String(200))
#     email = Column(String(200))
#     phone_number = Column(String(20))
#     flight = relationship("Flight", back_populates="flight_provider")
#
#
# class Flight(Base):
#     __tablename__ = "flight"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     name = Column(String(50), nullable=False)
#     description = Column(String(200))
#     departure_from = Column(String(200))
#     departure_to = Column(String(200))
#     departure_date = Column(DateTime)
#     arrival_date= Column(DateTime)
#     services = relationship("FlightServices", back_populates="flight")
#     flight_provider_id = Column(String(36), ForeignKey('flight_provider.id'), unique=True)
#     flight_provider = relationship("FlightProvider", back_populates="flight")
#     # created_at = Column(DateTime)
#     # updated_at = Column(DateTime)
#     # deleted_at = Column(DateTime)
#     # created_by = Column(Integer)
#     # updated_by = Column(Integer)
#     # deleted_by = Column(Integer)
#
# class FlightServices(Base):
#     __tablename__ = "flight_services"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     name = Column(String(50), nullable=False)
#     description = Column(String(2000))
#     seat_class = Column(String(50), nullable=False)
#     price_adult = Column(Integer)
#     price_child = Column(Integer)
#     price_baby = Column(Integer)
#     flight_id = Column(String(36), ForeignKey('flight.id'), unique=True)
#     flight = relationship("Flight", back_populates="services")
#     flight_booking = relationship("FlightBooking", back_populates="flight_services")
#     # created_at = Column(DateTime)
#     # updated_at = Column(DateTime)
#     # deleted_at = Column(DateTime)
#     # created_by = Column(Integer)
#     # updated_by = Column(Integer)
#     # deleted_by = Column(Integer)
#
# class FlightBooking(Base):
#     __tablename__ = "flight_booking"
#     id = Column(String(36), primary_key=True, default=generate_uuid(), unique=True)
#     payment_id = Column(String(36), ForeignKey('payment.id'), unique=True)
#     payment = relationship("Payment", back_populates="flight_booking")
#     flight_services_id = Column(String(36), ForeignKey('flight_services.id'), unique=True)
#     flight_services = relationship("FlightServices", back_populates="flight_booking")
#     number_of_adult = Column(Integer,default=0)
#     number_child = Column(Integer, default=0)
#     number_baby = Column(Integer, default=0)
#
