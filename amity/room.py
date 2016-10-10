from models.amity_database import Room as RoomClass, sess
from people import Person 
import random  

class Room(object):
    """ Class that can create rooms, randomly add people to rooms,
        check rooms for available space and reallocate people to different
        rooms 
    """
    list_of_offices = []
    list_of_living_spaces = [] 

    def __init__(self):
        # self.session = sess
        pass

    def create_room(self, room_name, room_type, room_capacity):
        new_room = RoomClass()
        new_room.room_name = room_name
        new_room.room_type = room_type
        new_room.room_capacity = room_capacity
        new_room.room_occupants = 0
        sess.add(new_room)
        sess.commit()

    def space_available(self):
        sa = sess.query(RoomClass).filter(RoomClass.room_name == room_name).one()
        if sa.room_occupants < sa.room_capacity:
            return True # There is space 
        return False # No space available 

    def add_person(self):
        room = Room() 
        offices = sess.query(RoomClass).filter(RoomClass.room_type == 'Office').all()
        list_of_offices.append(offices)
        for office in list_of_offices:
            is_there_space = room.space_available()
            if is_there_space:
                new_person.assigned_office = random.choice(list_of_offices) 
        sess.add(new_person.assigned_office)
        sess.commit()

    def reallocate_person():
    	pass

r1 = Room()
r1.create_room('Narnia', 'Office', 6)
