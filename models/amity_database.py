import os
import sys
from sqlalchemy import Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
db = create_engine('sqlite:////opt/projects/checkpoint_1/cp1.db') 
DBSession = sessionmaker() 
sess = DBSession() # Creates session object
DBSession.configure(bind=db) # Binds the db session to the engine


class Person(Base):
	"""Database containing Fellows and Staff"""
	__tablename__= "person"
	person_id = Column(Integer, primary_key=True)
	first_name = Column(String(15), index=True)
	last_name = Column(String(15))
	gender = Column(String(1)) # Restrict to either female or male
	job_group = Column(String(7), index=True)
	assigned_office = Column(String(15), index=True)
	assigned_living_space = Column(String(15), nullable=True, index=True)

class Room(Base):
	"""Database containing information on Living spaces and Offices"""
	__tablename__= "room"
	room_name = Column(String, primary_key=True)
	room_type = Column(String, index=True, )
	room_capacity = Column(Integer)
	room_occupants = Column(Integer)		

# Creates all the tables defined by models
Base.metadata.create_all(db)