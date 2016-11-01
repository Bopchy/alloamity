from models.amity_database import *


class Amity(object):

    """
    Class that print allocations of persons within amity, as well as
    unallocated fellows
    """

    def __init__(self, session):
        self.session = session
        self.rooms, self.persons = self.load_state()

    def load_state(self, db_name='default_alloamity_db.sqlite'):
        def rooms():
            return self.session.query(Room)

        def persons():
            return self.session.query(Person)

        return (rooms(), persons(),)

    def space_available(self, room_name):
        sa = rooms.filter_by(room_name=room_name).one()

        if sa.room_type == 'O':
            room_capacity = 6
        elif sa.room_type == 'L':
            room_capacity = 4

        if sa.room_occupants < room_capacity:
            return True  # There is space
        return False  # No space available

    def create_room(self, room_name, room_type):

        new_room = Room()
        new_room.room_name = room_name
        new_room.room_type = room_type
        new_room.room_occupants = 0
        self.session.add(new_room)

    def print_room(self, room_name):
        members_in_office = self.persons.filter_by(
            assigned_office=room_name).all()
        members_in_living_space = self.persons.filter_by(
            assigned_living_space=room_name).all()
        members_in_room = members_in_office + members_in_living_space

        [print(member.first_name + ' ' + member.last_name) for member in members_in_room]

    def print_allocations(self):
        existing_rooms = self.rooms.all()
        if len(existing_rooms) == 0:
            print('There are currently no existing rooms.')
        for room in existing_rooms:
            if room.room_type == 'O':
                members_of_the_room = self.persons.filter_by(assigned_office=room.room_name).all()
                print(room.room_name)
                print('-' * 30)
                if len(members_of_the_room) == 0:
                    print('This room is empty')
                member_names = [member.first_name + ' ' + member.last_name for member in members_of_the_room]
                print(', '.join(member_names) + '\n')

            else:
                members_of_the_room = self.persons.filter_by(assigned_living_space=room.room_name).all()
                print(room.room_name)
                print('-' * 30)
                if len(members_of_the_room) == 0:
                    print('This room is empty')
                member_names = [member.first_name + ' ' + member.last_name for member in members_of_the_room]
                print(', '.join(member_names) + '\n')

    def print_unallocated(self):  # Prints fellows that said N to want_accomodation
        unallocated = self.persons.filter_by(want_accomodation='N').all()
        if len(unallocated) == 0:
            print('There are currently no unallocated fellows.')
            return

        unallocated_fellows = [fellow.first_name + ' ' + fellow.last_name for fellow in unallocated]

        for fellow in unallocated_fellows:
            print(fellow)

    def save_state(self):
        self.session.commit()
        print('Your session has been saved.')


# Print list of all the fellows in Amity
# Print all the living spaces in Amity
# Print all offices
# Print a list of all the staff members in Amity

# r1 = Amity()
# # r1.create_room('New', 'L')
# r2 = Amity()
# # r2.create_room('Shire', 'O')
# r1.create_room('Winterfell', 'O')
# r2.create_room('Kings Landing', 'L')
# r1.print_room('Narnia')
# r1.print_allocations()
# r1.print_unallocated()

# Amity.save_state()

# a1 = Amity()
# a1.print_unallocated()
# Amity.print_unallocated()
# data = Amity.load_state(db)
# narnias = (data['Persons'].filter_by(assigned_office='Narnia').all())
# [print(narnia.first_name) for narnia in narnias]
# # print(data)
