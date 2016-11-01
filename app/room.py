from app.amity import Amity
from app.session import Session
from models.amity_database import Room as RoomModel, Person as PersonModel
from sqlalchemy.orm.exc import NoResultFound
import os
import random


class Room(Amity):

    """
    Class that create rooms, randomly adds people to rooms,
    check rooms for available space and reallocate people to different
    rooms.
    """

    list_of_offices = []
    list_of_living_spaces = []

    def __init__(self, session):
        self.session = session
        self.rooms, self.persons = self.load_state()

    def load_state(self):
        return super(Room, self).load_state(db_name='default_alloamity_db.sqlite')

    def space_available(self, room_name):
        return super(Room, self).space_available(room_name)
        # Will call this function through room.py, but using an Amity instance
        # because its super

        # super() ----> It is a “shortcut” to allow you to access the base class
        # of a derived class, without having to know or type the base class name.

    def add_person(self, first_name, last_name, job_group, want_accomodation='N', gender='N/A'):
        new_person = PersonModel()
        new_person.first_name = first_name
        new_person.last_name = last_name
        new_person.job_group = job_group
        new_person.want_accomodation = want_accomodation
        new_person.gender = gender

        self.add_person_to_office(new_person)

        if new_person.job_group == 'Fellow' and new_person.want_accomodation == 'Y':
            self.add_person_to_living_space(new_person)

        self.session.add(new_person)

    def add_person_to_office(self, new_person):
        the_offices = []
        self.list_of_offices = self.rooms.filter_by(room_type='O').all()

        for office in self.list_of_offices:
            is_there_office_space = super(Office, self).space_available(office.room_name)
            if is_there_office_space:
                the_offices.append(office)

        new_person.assigned_office = random.choice(the_offices).room_name
        # Is assigning an object from list of room objects query to
        # new_person.assigned_office

        rooms.filter_by(room_name=new_person.assigned_office)\
            .update({'room_occupants': Room.room_occupants+1})

    def add_person_to_living_space(self, new_person):
        the_living = []
        self.list_of_living_spaces = self.rooms.filter_by(room_type='L').all()

        for living_space in self.list_of_living_spaces:
            is_there_living_space = self.space_available(
                living_space.room_name)
            if is_there_living_space:
                the_living.append(living_space)

        new_person.assigned_living_space = random.choice(
            self.list_of_living_spaces).room_name
        rooms.filter_by(room_name=new_person.assigned_living_space)\
            .update({'room_occupants': RoomModel.room_occupants+1})


# r1.print_room('Narnia')
# Room.load_people('input1')
# r9 = Amity()
# r9.add_person('Noma', 'Bose', 'Fellow', 'Y', 'F')
# r9.reallocate_person('8', 'rom4')

# p = Room()
# p.add_person('usy', 'osy', 'Fellow', 'Y', 'F')
# p1 = Room()
# p1.add_person('Buy', 'Pie', 'Fellow', 'Y', 'M')
# p2 = Room()
# p2.add_person('Boo', 'Lin', 'Staff')
