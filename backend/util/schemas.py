from datetime import datetime, date

from pydantic import BaseModel


class UserBase(BaseModel):
    phone_number: str


class UserLogIn(UserBase):
    password: str


class UserUpdatePassword(UserLogIn):
    new_password: str


class UserSchemas(UserBase):
    # user_id: str=None
    password: str
    authorization: int


class UserVerify(UserSchemas):
    user_id: str = None


class UserProfileSchemas(BaseModel):
    # user_id: str
    # phone_number: str
    first_name: str
    last_name: str
    gender: bool
    email: str
    street: str
    city: str
    state: str
    zip_code: int
    country: str
    date_of_birth: date


class UserCardSchemas(BaseModel):
    # user_id: str
    card_number: str
    name_on_card: str
    cvv: str
    expiry_date: date


class UserCardID(BaseModel):
    id: str


class UserCardUpdateSchemas(UserCardID):
    id: str
    card_number: str
    name_on_card: str
    cvv: str
    expiry_date: date


class HotelCreate(BaseModel):
    name: str
    phone_number: str
    description: str
    address: str
    city: str
    state: str
    zip_code: str


class HotelUpdate(HotelCreate):
    id: str


class HotelDelete(BaseModel):
    id: str


class HotelServiceCreate(BaseModel):
    name: str
    room_type: str
    room_capacity: int
    description: str
    price: int
    hotel_id: str


class HotelServiceUpdate(HotelServiceCreate):
    id: str


class HotelServiceDelete(BaseModel):
    id: str


class HotelBookingCreate(BaseModel):
    user_id: str
    user_card_id: str
    hotel_services_id: str
    number_of_room: int
    check_in: date
    check_out: date
    payment_status: int
    payment_time: datetime
    payment_description: str


class HotelBookingUpdate(HotelBookingCreate):
    id: str


class HotelBookingDelete(BaseModel):
    id: str


class UserHotelRatingCreate(BaseModel):
    user_id: str
    hotel_id: str
    rating: int
    comment: str


class UserHotelRatingUpdate(UserHotelRatingCreate):
    id: str


class UserHotelRatingDelete(BaseModel):
    id: str


class FlightCreate(BaseModel):
    name: str
    description: str
    departure_from: str
    arrival_to: str
    departure_date: datetime
    arrival_date: datetime
    flight_provider_id: str


class FlightUpdate(FlightCreate):
    id: str


class FlightDelete(BaseModel):
    id: str


class FlightTicketCreate(BaseModel):
    name: str
    description: str
    seat_class: str
    adult_price: int
    child_price: int
    baby_price: int
    flight_id: str


class FlightTicketUpdate(FlightTicketCreate):
    id: str


class FlightTicketDelete(BaseModel):
    id: str


class FlightBookingCreate(BaseModel):
    user_id: str
    user_card_id: str
    departure_flight_ticket_id: str
    return_flight_ticket_id: str
    number_of_adult: int
    number_of_child: int
    number_of_baby: int
    payment_status: int
    payment_time: datetime
    payment_description: str


class FlightBookingUpdate(FlightBookingCreate):
    id: str


class FlightBookingDelete(BaseModel):
    id: str


class FlightProviderCreate(BaseModel):
    name: str
    description: str
    phone_number: str
    email: str


class FlightProviderUpdate(FlightProviderCreate):
    id: str


class FlightProviderDelete(BaseModel):
    id: str


class UserFlightProviderRatingCreate(BaseModel):
    user_id: str
    flight_id: str
    rating: int
    comment: str


class UserFlightProviderRatingUpdate(UserFlightProviderRatingCreate):
    id: str


class UserFlightProviderRatingDelete(BaseModel):
    id: str


# class FlightBookingCreate(BaseModel):
#     user_id : str
#     user_card_id : str
#     departure_flight_ticket_id : str
#     return_flight_ticket_id : str
#     number_of_adult : int
#     number_of_child : int
#     number_of_baby : int
#     payment_status : int
#     payment_time : datetime
#     payment_description : str
#
# class FlightBookingUpdate(FlightBookingCreate):
#     id: str
#
# class FlightBookingDelete(BaseModel):
#     id: str


class TourCreate(BaseModel):
    name: str
    description: str
    duration: int
    destination: str
    adult_price: int
    child_price: int


class TourUpdate(TourCreate):
    id: str


class TourDelete(BaseModel):
    id: str


class TourBookingCreate(BaseModel):
    user_id: str
    user_card_id: str
    tour_date_id: str
    number_of_adult: int
    number_of_child: int
    payment_status: int
    payment_time: datetime
    payment_description: str


class TourBookingUpdate(TourBookingCreate):
    id: str


class TourBookingDelete(BaseModel):
    id: str


class TourDateCreate(BaseModel):
    tour_id: str
    departure_datetime: datetime
    return_datetime: datetime


class TourDateUpdate(TourDateCreate):
    id: str


class TourDateDelete(BaseModel):
    id: str

class UserSchemasCustomer(BaseModel):
    phone_number: str
    password: str
