import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DatabaseCreate(object):
	def __init__(self, db_name=None):
		self.db_name = db_name
		if self.db_name:
			self.engine = create_engine('sqlite:///'+ self.db_name + '.sqlite')
			print('Your database' + db_name + ' has been created')
	
		else:
			self.engine = create_engine('sqlite:///default_alloamity_db.sqlite')
		
		DBSession = sessionmaker(bind=self.engine)
		self.session = DBSession()
		Base.metadata.create_all(self.engine)

DC = DatabaseCreate()

class Person(Base):
	""" 
	Database table containing Fellows and Staff
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

class Room(Base):
	""" 
	Database table containing information on Living spaces and Offices
	"""
	__tablename__= "room"
	id = Column(Integer, primary_key=True)
	room_name = Column(String, unique=True)
	room_type = Column(String(1), index=True)
	room_occupants = Column(Integer, default=0)

# Creates all the tables defined by models
# Base.metadata.create_all(db)

# p = os.path.dirname(__file__)
r = DatabaseCreate()