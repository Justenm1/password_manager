from sqlalchemy import create_engine, ForeignKey, String, Column
from sqlalchemy.orm import declarative_base, sessionmaker
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Users(Base):
    __tablename__ = 'users'

    user_id = Column("user_id", String, primary_key=True, default=generate_uuid)
    username = Column("username", String)
    password = Column("password", String)
    role = Column("role", String)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class user_entries(Base):
    __tablename__ = 'user_entries'

    user_id = Column("user_id", String, ForeignKey('users.user_id'))
    site_id = Column("site_id", String, primary_key=True, default=generate_uuid)
    site = Column("site", String)
    site_username = Column("site_username", String)
    site_password = Column("site_password", String)

    def __init__(self, user_id=None, site=None, site_username=None, site_password=None):
        self.user_id = user_id
        self.site = site
        self.site_username = site_username
        self.site_password = site_password

def adduser(session, username, password, role):
    # create a user
    exists = session.query(Users).filter(Users.username == username).scalar()
    if exists != None:
        print("User already exists")
    else:
        user = Users(username=username, password=password, role=role)
        session.add(user)
        session.commit()
        print(f"User {username} added to db successfully")


def adduserentry(session, user_id, site, site_username, site_password):
    # Create a user entry
    userentry = user_entries(site=site, site_username=site_username, site_password=site_password)
    session.add(userentry)
    session.commit()
    print("Entry added successfully")


db = "sqlite:///users.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()