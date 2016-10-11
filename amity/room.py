from models.amity_database import Room as RoomClass, Person as PersonClass, sess 
from models.amity_database import RoomMembers 
from sqlalchemy.orm.exc import NoResultFound
import random  

class Room(object):
    """ Class that can create rooms, randomly add people to rooms,
        check rooms for available space and reallocate people to different
        rooms 
    """
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
        try:
            sa = sess.query(RoomClass).filter_by(room_name=room_name).one() 
        except NoResultFound:
            """Handle exception"""
        
        if sa.room_occupants < sa.room_capacity:
            return True # There is space 
        return False # No space available 

    def add_person(self, new_person):         
        self.add_person_to_office(new_person)
        if new_person.job_group == 'Fellow' and new_person.want_accomodation == 'Y':
            self.add_person_to_living_space(new_person)

    def add_person_to_office(self, new_person):
        the_offices = []
        self.list_of_offices = sess.query(RoomClass).filter_by(room_type='Office').all()               
        
        for office in self.list_of_offices:
            is_there_office_space = self.space_available(office.room_name)
            if is_there_office_space:
                the_offices.append(office)

        new_person.assigned_office = random.choice(the_offices).room_name 
        # Is assigning an object from list of room objects query to 
        # new_person.assigned_office
        sess.query(RoomClass)\
            .filter_by(room_name=new_person.assigned_office)\
            .update({'room_occupants': RoomClass.room_occupants+1})

    def add_person_to_living_space(self, new_person):
        the_living = []
        self.list_of_living_spaces = sess.query(RoomClass).filter_by(room_type='Living Space').all()
        
        for living_space in self.list_of_living_spaces:
            is_there_living_space = self.space_available(living_space.room_name)
            if is_there_living_space:
                the_living.append(living_space)

        new_person.assigned_living_space = random.choice(self.list_of_living_spaces).room_name
        sess.query(RoomClass).filter_by(room_name=new_person.assigned_living_space)\
            .update({'room_occupants': RoomClass.room_occupants+1})

    def reallocate_person(self, person_id, room_name):
        try:
            person_details = sess.query(PersonClass).filter_by(person_id=person_id).one()
            room_details = sess.query(RoomClass).filter_by(room_name=room_name).one()
            room_type = room_details.room_type
            space_status = self.space_available(room_name)
            if space_status:
                if room_type == 'Office':
                    current_room = person_details.assigned_office
                    sess.query(PersonClass).filter_by(person_id=person_id).update({'assigned_office':room_name})
                    sess.query(RoomClass).filter_by(room_name=room_name).update({'room_occupants':room_details.room_occupants+1})
                    sess.query(RoomClass).filter_by(room_name=current_room).update({'room_occupants':RoomClass.room_occupants-1})

                elif room_type == 'Living Space':
                    current_room = person_details.assigned_living_space
                    sess.query(PersonClass).filter_by(person_id=person_id).update({'assigned_living_space':room_name})
                    sess.query(RoomClass).filter_by(room_name=room_name).update({'room_occupants':room_details.room_occupants+1})
                    sess.query(RoomClass).filter_by(room_name=current_room).update({'room_occupants':RoomClass.room_occupants-1})

        except NoResultFound:
            '''Recored not found'''
        sess.commit()       

    def remove_person_from_room(self, person_id, room_name):
        # checker = sess.query(RoomMembers).filter_by(person_id=person_id, room_name=room_name).first()
        # .delete()
        # sess.commit()
        pass 


r1 = Room()
# r1.create_room('Narnia', 'Office', 6)
# r2 = Room()
# r2.create_room('Krypton', 'Office', 6)
# r3 = Room()
# r3.create_room('Shire', 'Office', 6)
# r4 = Room()
# r4.create_room('Ruby', 'Living Space', 4)
# r5 = Room()
# r5.create_room('Topaz', 'Living Space', 4)
# r6 = Room()
# r6.create_room('Jade', 'Living Space', 4)

# r8 = Room()
# r8.space_available('Narnia')

r1.reallocate_person(5, 'Narnia')
