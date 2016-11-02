import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):

    """ Database table containing Fellows and Staff"""
    __tablename__ = "person"
    person_id = Column(Integer, primary_key=True)
    first_name = Column(String(15), index=True)
    last_name = Column(String(15))
    gender = Column(String(1))  # Restrict to either female or male
    job_group = Column(String(7), index=True)
    assigned_office = Column(String(15), index=True)
    assigned_living_space = Column(String(15), nullable=True, index=True)
    want_accomodation = Column(String(1), nullable=True)


class Room(Base):

    """ Database table containing information on Living spaces and Offices"""
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    room_name = Column(String, unique=True)
    room_type = Column(String(1), index=True)
    room_occupants = Column(Integer, default=0)
