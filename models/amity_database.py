import os
import sys

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):

    """ Database table containing Fellows and Staff"""
    __tablename__ = "person"
    person_id = Column(Integer, primary_key=True)
    full_name = Column(String(50), index=True)
    job_group = Column(String(7), index=True)
    want_accomodation = Column(String(1), nullable=True)
    assigned_office = Column(String(15), index=True)
    assigned_living_space = Column(String(15), nullable=True, index=True)


# class UnallocatedPerson(Base):

#     """Database table containing Unallocated Persons"""
#     __tablename__ = "unallocated_person"
#     person_id = Column(Integer, primary_key=True)
#     full_name = Column(String(50), index=True)
#     job_group = Column(String(7), index=True)
#     want_accomodation = Column(String(1), nullable=True)
#     assigned_office = Column(String(15), index=True)
#     assigned_living_space = Column(String(15), nullable=True, index=True)


class Room(Base):

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

    def create_session(self, db_name='alloamity_db.sqlite'):
        DBSession = sessionmaker(bind=self.engine, autoflush=False)
        self.session = DBSession()
        return self.session

    def create_database(self, db_name='alloamity_db.sqlite'):
        sessionmaker(bind=self.engine, autoflush=False)
        Base.metadata.create_all(self.engine)
        return True
