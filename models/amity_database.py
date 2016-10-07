import os
import sys
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine 

Base = declarative_base() 

class Amity(Base):
	"""General database for Amity Office Allocation system"""
	__tablename__= "amity"
		id = Column(Integer, primary_key=True)
		
		def print_allocations():
			pass

class Person(Base):
	"""Database containing Fellows and Staff"""
	__tablename__= "person"
	id = Column(Integer, primary_key=True)

class Room(Base):
	"""Database containing information on Living spaces and Offices"""
	__tablename__= "room"
	room_name = Column(String, primary_key=True)


		
		
		

