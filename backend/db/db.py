from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


from backend.db.model import Base, User


# from model import User,Base
connection_string = "mysql+mysqlconnector://root:mocbop123@localhost/travel_agency_v1"
engine = create_engine(connection_string, echo=True)


@contextmanager
def session_scope() -> Session:
    """Provide a transactional scope around a series of operations."""
    db = None
    try:
        db = Session(autocommit=False, autoflush=False,
                     bind=engine)  # create session from SQLModel session
        yield db
    finally:
        db.close()

#create new tables
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
#
# # insert data
#
# with session_scope() as session:
#     # user1=User(fullname="dfs",sex=1,phone_number="123",email="fsdf",password="123")
#     # user2=User(name='dfsf',fullname="dfrdgs",sex=1,phone_number="1253",email="fasdf")
#     # session.add(user1)
#     #
#     # session.add(user2)
#     user1=session.query(User).filter(User.phone_number=="123").first()
#     # session.commit()
#     print("user1.id:",user1.id)





