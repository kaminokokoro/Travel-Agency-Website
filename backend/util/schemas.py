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