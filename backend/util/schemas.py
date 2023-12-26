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
    authorization:int

class UserVerify(UserSchemas):
    user_id: str=None

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
    card_number : str
    name_on_card : str
    cvv : str
    expiry_date : date

class UserCardID(BaseModel):
    id:str

class UserCardUpdateSchemas(UserCardID):
    id:str
    card_number : str
    name_on_card : str
    cvv : str
    expiry_date : date

class HotelCreate(BaseModel):
    name : str
    phone_number : str
    description : str
    address : str
    city : str
    state : str
    zip_code :str

class HotelUpdate(HotelCreate):
    id : str

class HotelDelete(BaseModel):
    id : str



class HotelServiceCreate(BaseModel):
    name : str
    room_type : str
    room_capacity: int
    description : str
    price : int
    hotel_id : str

class HotelServiceUpdate(HotelServiceCreate):
    id : str

class HotelServiceDelete(BaseModel):
    id : str



class HotelBookingCreate(BaseModel):
    user_id : str
    user_card_id : str
    hotel_services_id : str
    number_of_room : int
    check_in : date
    check_out : date
    payment_status : int
    payment_time : datetime
    payment_description : str

class HotelBookingUpdate(HotelBookingCreate):
    id : str

class HotelBookingDelete(BaseModel):
    id : str


