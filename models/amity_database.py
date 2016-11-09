import os
import sys
<<<<<<< Updated upstream
from sqlalchemy import Column, Integer, String, ForeignKey 
=======

from sqlalchemy import Column, Integer, String, ForeignKey
>>>>>>> Stashed changes
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()
db = create_engine('sqlite:////opt/projects/checkpoint_1/cp1.db') 
DBSession = sessionmaker() 
DBSession.configure(bind=db) # Binds the db session to the engine
sess = DBSession() # Creates session object

class Person(Base):
<<<<<<< Updated upstream
	""" Database table containing Fellows and Staff
	"""
	__tablename__= "person"
	person_id = Column(Integer, primary_key=True)
	first_name = Column(String(15), index=True)
	last_name = Column(String(15))
	gender = Column(String(1)) # Restrict to either female or male
	job_group = Column(String(7), index=True)
	assigned_office = Column(String(15), index=True)
	assigned_living_space = Column(String(15), nullable=True, index=True)
	want_accomodation = Column(String(1), nullable=True)
	
=======

    """ Database table containing Fellows and Staff"""
    __tablename__ = "person"
    person_id = Column(Integer, primary_key=True)
    first_name = Column(String(15), index=True)
    last_name = Column(String(15))
    job_group = Column(String(7), index=True)
    want_accomodation = Column(String(1), nullable=True)
    assigned_office = Column(String(15), index=True)
    assigned_living_space = Column(String(15), nullable=True, index=True)

>>>>>>> Stashed changes

class Room(Base):
	""" Database table containing information on Living spaces and Offices
	"""
	__tablename__= "room"
	id = Column(Integer, primary_key=True)
	room_name = Column(String, unique=True)
	room_type = Column(String, index=True, )
	room_capacity = Column(Integer)
	room_occupants = Column(Integer, default=0)

class RoomMembers(Base):
	""" Database table containing the room members in a particular room 
	"""	
	__tablename__= "room_members"
	id = Column(Integer, primary_key=True)
	
	person_id = Column(Integer, ForeignKey("person.person_id"))
	room_members = relationship("Person", backref=backref("person", lazy="dynamic"))
	
	room_name = Column(String, ForeignKey("room.room_name"))
	persons_in_room = relationship("Room", backref=backref("room", lazy="dynamic"))

<<<<<<< Updated upstream
# Creates all the tables defined by models
Base.metadata.create_all(db)
=======
    """ Database table containing information on Living spaces and Offices"""
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    room_name = Column(String, unique=True)
    room_type = Column(String(1), index=True)
    room_occupants = Column(Integer, default=0)


class Session(object):

    def __init__(self, db_name=None):
        self.db_name = db_name
        if self.db_name:
            self.engine = create_engine('sqlite:///' + self.db_name + '.sqlite')
            print('Your database' + db_name + ' has been created')

        else:
            self.engine = create_engine('sqlite:///alloamity_db.sqlite')

    def create_session(self):
        DBSession = sessionmaker(bind=self.engine, autoflush=False)
        self.session = DBSession()
        return self.session

    def create_database(self, db_name='alloamity_db.sqlite'):
        sessionmaker(bind=self.engine, autoflush=False)
        Base.metadata.create_all(self.engine)
        return True
>>>>>>> Stashed changes
