from datetime import datetime, date

from pydantic import BaseModel


class UserBase(BaseModel):
    phone_number: str
class UserLogIn(UserBase):
    password: str

class UserUpdatePassword(UserLogIn):
    new_password: str

class UserSchemas(UserBase):
    password: str
    authorization:int
class UserProfileSchemas(BaseModel):
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
    card_number : str
    name_on_card : str
    cvv : str
    expiry_date : date