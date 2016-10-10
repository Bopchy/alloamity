from models.amity_database import Room as RoomClass, Person as PersonClass, sess 
# from people import Person
import random  

class Room(object):
    """ Class that can create rooms, randomly add people to rooms,
        check rooms for available space and reallocate people to different
        rooms 
    """
    # self.session = sess
    list_of_offices = []
    list_of_living_spaces = []

    def create_room(self, room_name, room_type, room_capacity):
        new_room = RoomClass()
        new_room.room_name = room_name
        new_room.room_type = room_type
        new_room.room_capacity = room_capacity
        new_room.room_occupants = 0
        sess.add(new_room)
        sess.commit()

    def space_available(self, room_name):
        sa = sess.query(RoomClass).filter_by(room_name=room_name).one()
        if sa.room_occupants < sa.room_capacity:
            return True # There is space 
        return False # No space available 

    def add_person(self, new_person):         
        self.list_of_offices = sess.query(RoomClass).filter_by(room_type='Office').all()
                        
        for office in self.list_of_offices:
            is_there_office_space = self.space_available(office.room_name)

            if is_there_office_space:
                new_person.assigned_office = random.choice(self.list_of_offices).room_name # Is assigning an object from list of room objects queries 
                sess.query(RoomClass)\
                    .filter_by(room_name=new_person.assigned_office)\
                    .update({'room_occupants': RoomClass.room_occupants+1})

        if new_person.job_group == 'Fellow' and new_person.want_accomodation == 'Y':
            self.list_of_living_spaces = sess.query(RoomClass).filter_by(room_type='Living Space').all()
            for living_space in self.list_of_living_spaces:
                is_there_living_space = self.space_available(living_space.room_name)
                if is_there_living_space:
                    new_person.assigned_living_space = random.choice(self.list_of_living_spaces).room_name
                    sess.query(RoomClass).filter_by(room_name=new_person.assigned_living_space)\
                        .update({'room_occupants': RoomClass.room_occupants+1})

    def reallocate_person():
    	


# r1 = Room()
# r1.create_room('Narnia', 'Office', 6)
# r2 = Room()
# r2.create_room('Krypton', 'Office', 6)
# r3 = Room()
# r3.create_room('Shire', 'Office', 6)
