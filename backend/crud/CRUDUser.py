from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from backend.db.db import session_scope
from backend.db.model import User, UserProfile, UserCard, generate_uuid
from backend.util import passutil, schemas
from backend.util.schemas import UserProfileSchemas, UserCardSchemas, UserSchemas


class CRUDUser():

    def create_user(self, user: schemas.UserSchemas):
        try:
            with session_scope() as db:
                user_id = generate_uuid()
                user = User(id=user_id, phone_number=user.phone_number,
                            password=passutil.get_password_hash(user.password),
                            authorization=user.authorization)
                db.add(user)
                db.commit()
                db.refresh(user)
                return user
        except SQLAlchemyError as e:
            print(e)
            return None

    def get_user_by_phone_number(self, phone_number) -> User:
        try:
            with session_scope() as db:
                user = db.query(User).filter(User.phone_number == phone_number).first()
                return user
        except SQLAlchemyError as e:
            print(e)
            return None

    def get_user_by_id(self, user_id) -> User:
        try:
            with session_scope() as db:
                user = db.query(User).filter(User.id == user_id).first()
                return user
        except SQLAlchemyError as e:
            print(e)
            return None

    def update_user_password(self, user_id: str, new_password: str):
        try:
            with session_scope() as db:
                user = db.query(User).filter(User.id == user_id).first()
                user.password = passutil.get_password_hash(new_password)
                db.commit()
                db.refresh(user)
                return user
        except SQLAlchemyError as e:
            print(e)
            return None

    def delete_user_account(self, user_id: str):
        try:
            with session_scope() as db:
                user = db.query(User).filter(User.id == user_id).first()
                db.delete(user)
                db.commit()
                return user
        except SQLAlchemyError as e:
            print(e)
            return None

    def get_all_user(self, page_number: int, page_size: int):
        try:
            with session_scope() as db:
                users = db.query(User).offset((page_number - 1) * page_size).limit(page_size).all()
                return users
        except SQLAlchemyError as e:
            print(e)
            return None

    def get_user_profile(self, user_id: str):
        try:
            with session_scope() as db:
                user_profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
                return user_profile
        except SQLAlchemyError as e:
            print(e)
            return None

    def create_user_profile(self, user_id: str, user_profile_schemas: UserProfileSchemas):
        try:
            with session_scope() as db:
                user_profile = UserProfile()
                user_profile.id = generate_uuid()
                user_profile.first_name = user_profile_schemas.first_name
                user_profile.last_name = user_profile_schemas.last_name
                user_profile.gender = user_profile_schemas.gender
                user_profile.email = user_profile_schemas.email
                user_profile.street = user_profile_schemas.street
                user_profile.city = user_profile_schemas.city
                user_profile.state = user_profile_schemas.state
                user_profile.zip_code = user_profile_schemas.zip_code
                user_profile.country = user_profile_schemas.country
                user_profile.date_of_birth = user_profile_schemas.date_of_birth
                user_profile.user_id = user_id
                db.add(user_profile)
                db.commit()
                db.refresh(user_profile)
                return user_profile
        except SQLAlchemyError as e:
            print(e)
            return None

    def update_user_profile(self, user_id, user_profile_schemas: UserProfileSchemas):
        try:
            with session_scope() as db:

                user_profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
                user_profile.first_name = user_profile_schemas.first_name
                user_profile.last_name = user_profile_schemas.last_name
                user_profile.gender = user_profile_schemas.gender
                user_profile.email = user_profile_schemas.email
                user_profile.street = user_profile_schemas.street
                user_profile.city = user_profile_schemas.city
                user_profile.state = user_profile_schemas.state
                user_profile.zip_code = user_profile_schemas.zip_code
                user_profile.country = user_profile_schemas.country
                user_profile.date_of_birth = user_profile_schemas.date_of_birth
                db.commit()
                db.refresh(user_profile)
                return user_profile
        except SQLAlchemyError as e:
            print(e)
            return None

    def create_user_card(self, user_id: str, user_card_schemas: UserCardSchemas):
        try:
            with session_scope() as db:
                user_card = UserCard()
                user_card.id = generate_uuid()
                user_card.card_number = user_card_schemas.card_number
                user_card.name_on_card = user_card_schemas.name_on_card
                user_card.cvv = user_card_schemas.cvv
                user_card.expiry_date = user_card_schemas.expiry_date
                user_card.user_id = user_id
                db.add(user_card)
                db.commit()
                db.refresh(user_card)
                return user_card
        except SQLAlchemyError as e:
            print(e)
            return None

    def get_all_user_card(self, user_id: str):
        try:
            with session_scope() as db:
                user_card = db.query(UserCard).filter(UserCard.user_id == user_id).all()
                return user_card
        except SQLAlchemyError as e:
            print(e)
            return None

    def update_user_card(self, user_id: str,card_id:str ,user_card_schemas: UserCardSchemas):
        try:
            with session_scope() as db:
                user_card = db.query(UserCard).filter(and_(UserCard.user_id == user_id, UserCard.id == card_id)).first()
                user_card.card_number = user_card_schemas.card_number
                user_card.name_on_card = user_card_schemas.name_on_card
                user_card.cvv = user_card_schemas.cvv
                user_card.expiry_date = user_card_schemas.expiry_date

                db.commit()
                db.refresh(user_card)
                return user_card
        except SQLAlchemyError as e:
            print(e)
            return None

    def delete_user_card(self, user_id: str, card_id):
        try:
            with session_scope() as db:
                user_card = db.query(UserCard).filter(and_(UserCard.user_id == user_id, UserCard.id == card_id)).first()
                db.delete(user_card)
                db.commit()
                return user_card
        except SQLAlchemyError as e:
            print(e)
            return None


crud_user = CRUDUser()
user = UserSchemas(phone_number="123456789", password="123456789", authorization=3)
crud_user.create_user(user)
user1 = UserSchemas(phone_number="12345678", password="12345678", authorization=2)
crud_user.create_user(user1)
# crud_user.create_user("123","123",1)
# crud_user.update_user_password("123","1234")
# crud_user.create_user_card("123",UserCardSchemas(card_number="123",name_on_card="123",cvv="123",expiry_date=datetime.date(2021,1,1)))
# crud_user.update_user_card("123",UserCardSchemas(card_number="1234",name_on_card="1234",cvv="1234",expiry_date=datetime.date(2021,1,1)))
# crud_user.create_user_profile("123",UserProfileSchemas(first_name='a',last_name='b',gender=1,email='a',street='a',city='a',state='a',zip_code=1,country='a',date_of_birth=datetime.date(2021,1,1)))
# crud_user.update_user_profile("123",UserProfileSchemas(first_name='as',last_name='bs',gender=1,email='a',street='a',city='as',state='as',zip_code=12,country='as',date_of_birth=datetime.date(2021,1,1)))
# crud_user.get_user_profile("123")
# crud_user.get_user_card("123")
# crud_user.get_user_by_phone_number("123")
# crud_user.update_user_password("123","1234")
# crud_user.create_user("1234","123",1)
# crud_user.get_user_by_phone_number("123")
# crud_user.delete_user_account("123")

# # crud_user.create_user("123","123",1)
# crud_user.update_user_password("123","1234")
# crud_user.create_user_card("123",UserCardSchemas(card_number="123",name_on_card="123",cvv="123",expiry_date="2021-01-01"))
# crud_user.update_user_card("123",UserCardSchemas(card_number="1234",name_on_card="1234",cvv="1234",expiry_date="2021-01-01"))
# crud_user.create_user_profile()
# crud_user.update_user_profile()
# crud_user.get_user_profile("123")
# crud_user.get_user_card("123")
# crud_user.get_user_by_phone_number("123")
# crud_user.update_user_password("123","1234")
# crud_user.create_user("123","123",1)
# crud_user.get_user_by_phone_number("123")
# crud_user.delete_user_account("123")
# crud_user.create_user("123","123",1)
# crud_user.update_user_password("123","1234")
# crud_user.create_user_card("123",UserCardSchemas(card_number="123",name_on_card="123",cvv="123",expiry_date="2021-01-01"))
# crud_user.update_user_card("123",UserCardSchemas(card_number="1234",name_on_card="1234",cvv="1234",expiry_date="2021-01-01"))
# crud_user.create_user_profile()
# crud_user.update_user_profile()
# crud_user.get_user_profile("123")
# crud_user.get_user_card("123")
# crud_user.get_user_by_phone_number("123")
# crud_user.update_user_password("123","1234")
# crud_user.create_user("123","123",1)
# crud_user.get_user_by_phone_number("123")
# crud_user.delete_user_account("123")
# crud_user.create_user("123","123",1)
# crud_user.update_user_password("123","1234")
# crud_user.create_user_card("123",UserCardSchemas(card_number="123",
# crud_user.delete_user_account("123")
