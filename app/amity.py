from app.livingspace import LivingSpace
from app.office import Office
from models.session import Session
from models.amity_database import *
from app.people import Person


session = Session().create_session()
# Initializes a session with the database, so that load_state()
# loads data into the app, from the main database alloamity_db


class Amity(object):

    """Class Amity"""
    rooms = []
    persons = []

    def __init__(self, session):
        self.session = session
        # self.rooms, self.people = self.load_state()

    def load_state(self, db_name='alloamity_db.sqlite'):
        rooms = []
        persons = []

        def rooms():
            all_rooms = self.session.query(Room).all()
            rooms.append(all_rooms)

        def persons():
            all_persons = self.session.query(Person)
            persons.append(all_persons)

        return rooms, persons

    def space_available(self, room_name):
        # sa = rooms.filter_by(room_name=room_name).one()

        # if sa.room_type == 'O':
        #     room_capacity = Office().room_capacity
        # elif sa.room_type == 'L':
        #     room_capacity = LivingSpace().room_capacity

        # if sa.room_occupants < room_capacity:
        #     return True  # There is space
        # return False  # No space available
        pass

    def create_room(self, room_name, room_type):  # Fix it such that you can add multiple rooms at once
        # new_room = Room()
        # new_room.room_name = room_name
        # new_room.room_type = room_type
        # new_room.room_occupants = 0
        # rooms.append(new_room)
        pass

    def add_person(
            self,
            first_name,
            last_name,
            job_group,
            want_accomodation='N'
    ):
        # new_person = Person()
        # new_person.first_name = first_name
        # new_person.last_name = last_name
        # new_person.job_group = job_group
        # new_person.want_accomodation = want_accomodation
        # assigned_office = self.add_person_to_office(new_person)
        # assigned_living_space = self.add_person_to_living_space(new_person)

        # if new_person.job_group == 'Fellow' and new_person.want_accomodation == 'Y':
        #     self.add_person_to_living_space(new_person)

        # self.session.add(new_person)
        pass

    def add_person_to_office(self, new_person):
        # the_offices = []
        # self.list_of_offices = self.rooms.filter_by(room_type='O').all()

        # for office in self.list_of_offices:
        #     is_there_office_space = super(
        #         Office, self).space_available(
        #         office.room_name)
        #     if is_there_office_space:
        #         the_offices.append(office)

        # new_person.assigned_office = random.choice(the_offices).room_name
        # Is assigning an object from list of room objects query to
        # new_person.assigned_office

        # rooms.filter_by(room_name=new_person.assigned_office)\
        #     .update({'room_occupants': Room.room_occupants + 1})
        pass

    def add_person_to_living_space(self, new_person):
        # the_living = []
        # self.list_of_living_spaces = self.rooms.filter_by(room_type='L').all()

        # for living_space in self.list_of_living_spaces:
        #     is_there_living_space = self.space_available(
        #         living_space.room_name)
        #     if is_there_living_space:
        #         the_living.append(living_space)

        # new_person.assigned_living_space = random.choice(
        #     self.list_of_living_spaces).room_name
        # rooms.filter_by(room_name=new_person.assigned_living_space)\
        #     .update({'room_occupants': RoomModel.room_occupants + 1})
        pass

    @staticmethod
    def load_people(txt_file):
        # file_name = txt_file
        # with open(file_name) as file:
        #     for line in file.readlines():
        #         person = line.replace('\n', '').split()
        #         print(person)
        #         Room().add_person(*person)
                # Using python splat to add members of list as arguments to
                # add_person()
        pass

    def print_room(self, room_name):
        # members_in_office = self.persons.filter_by(
        #     assigned_office=room_name).all()
        # members_in_living_space = self.persons.filter_by(
        #     assigned_living_space=room_name).all()
        # members_in_room = members_in_office + members_in_living_space

        # [print(member.first_name + ' ' + member.last_name)
        #  for member in members_in_room]
        pass

    def print_allocations(self, file_name=''):
        # existing_rooms = self.rooms.all()
        # if len(existing_rooms) == 0:
        #     print('There are currently no existing rooms.')
        # for room in existing_rooms:
        #     if room.room_type == 'O':
        #         members_of_the_room = self.persons.filter_by(
        #             assigned_office=room.room_name).all()
        #         print(room.room_name)
        #         print('-' * 30)
        #         if len(members_of_the_room) == 0:
        #             print('This room is empty')
        #         member_names = [
        #             member.first_name +
        #             ' ' +
        #             member.last_name for member in members_of_the_room]
        #         print(', '.join(member_names) + '\n')

        #     else:
        #         members_of_the_room = self.persons.filter_by(
        #             assigned_living_space=room.room_name).all()
        #         print(room.room_name)
        #         print('-' * 30)
        #         if len(members_of_the_room) == 0:
        #             print('This room is empty')
        #         member_names = [
        #             member.first_name +
        #             ' ' +
        #             member.last_name for member in members_of_the_room]
        #         print(', '.join(member_names) + '\n')
        pass

    def reallocate_person(self, person_id, room_name):
        # person_details = persons.filter_by(person_id=person_id).one()
        # room_details = rooms.filter_by(room_name=room_name).one()
        # room_type = room_details.room_type
        # space_status = Room().space_available(room_name)
        # if space_status:
        #     if room_type == 'O':
        #         current_room = person_details.assigned_office
        #         persons.filter_by(person_id=person_id).update(
        #             {'assigned_office': room_name})
        #         rooms.filter_by(room_name=room_name).update(
        #             {'room_occupants': room_details.room_occupants + 1})
        #         rooms.filter_by(room_name=current_room).update(
        #             {'room_occupants': RoomModel.room_occupants - 1})

        #     elif room_type == 'L':
        #         current_room = person_details.assigned_living_space
        #         persons.filter_by(person_id=person_id).update(
        #             {'assigned_living_space': room_name})
        #         rooms.filter_by(room_name=room_name).update(
        #             {'room_occupants': room_details.room_occupants + 1})
        #         rooms.filter_by(room_name=current_room).update(
        #             {'room_occupants': RoomModel.room_occupants - 1})
        pass

    def print_unallocated(self, file_name=''):
        # unallocated = self.persons.filter_by(want_accomodation='N').all()
        # if len(unallocated) == 0:
        #     print('There are currently no unallocated fellows.')
        #     return

        # unallocated_fellows = [
        #     fellow.first_name +
        #     ' ' +
        #     fellow.last_name for fellow in unallocated]

        # for fellow in unallocated_fellows:
        #     print(fellow)
        pass

    def exit_room(self, person_id, room_name):
        person_details = persons.filter_by(person_id=person_id).one()
        person_office_details = persons.filter(assigned_office)
        person_living_space_details = person_details.filter(
            assigned_living_space)
        try:
            if person_office_details is room_name:
                persons.filter_by(assigned_office=room_name).update(
                    {'assigned_office': 'NULL'})
            if person_living_space_details is room_name:
                persons.filter_by(assigned_living_space=room_name).update(
                    {'assigned_living_space': 'NULL'})
        except Exception:
            return 'Person' + person_id + 'is not in that room.'

    def save_state(self, db='alloamity_db.sqlite'):
        self.session.add()
        self.session.commit()
        print('Your session has been saved.')
