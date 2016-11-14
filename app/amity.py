import random
import os

from models.amity_database import Room, Person as PersonModel, Session
from app.people import Person


session = Session().create_session()


class Amity(object):

    """Class Amity"""
    rooms = []
    persons = []
    unallocated = []

    def __init__(self, session):
        """Initializes a session with the database, so that load_state()
        loads data into the app, from the main database alloamity_db"""
        self.session = session

    def load_state(self, db_name='alloamity_db.sqlite'):
        """Loads data into application from database."""
        if os.path.exists('alloamity_db.sqlite'):
            all_rooms = self.session.query(Room).all()
            for list_all_rooms in all_rooms:
                Amity.rooms.append(list_all_rooms)

            all_persons = self.session.query(PersonModel).all()
            for list_all_persons in all_persons:
                Amity.persons.append(list_all_persons)

            os.remove('alloamity_db.sqlite')
            print('Data has been loaded into AlloAmity.')
            return True

        else:
            print("Database doesn't exist.")
            return False

    def add_person(
        self,
        first_name,
        last_name,
        job_group,
        want_accomodation='N'
    ):
        """Adds person into an office and living space randomly."""
        if job_group.lower() not in ['staff', 'fellow']:
            print(
                'Invalid input for job_group. Use: FELLOW for fellow, or STAFF for staff.')
            return False

        if want_accomodation.lower() not in ['y', 'n', 'yes', 'no']:
            print('Invalid input for want_accomodation. Use: Y for yes, or N for no.')
            return False

        new_person = Person()
        new_person._id = str(len(Amity.persons) + 1)
        new_person.first_name = first_name.upper()
        new_person.last_name = last_name.upper()
        new_person.job_group = job_group
        new_person.want_accomodation = want_accomodation.upper()
        self.add_person_to_office(new_person)
        self.add_person_to_living_space(new_person)

        Amity.persons.append(new_person)

    def add_person_to_office(self, new_person):
        """Adds person to an office randomly."""
        available_offices = []

        for room in Amity.rooms:
            if room.room_type == 'O' and room.room_occupants < 6:
                available_offices.append(room)

        if not available_offices:
            Amity.unallocated.append(new_person)
            print('No offices available. Person added to unallocated.')
            new_person.assigned_office = 'NULL'
            return False

        new_person.assigned_office = random.choice(available_offices).room_name

        for room in Amity.rooms:
            if room.room_name == new_person.assigned_office:
                room.room_occupants += 1
        print(new_person.first_name + ' ' + new_person.last_name +
              ' has been added to ' + new_person.assigned_office)
        return True

    def add_person_to_living_space(self, new_person):
        """Adds person to a living space randomly."""
        available_living_spaces = []

        for room in Amity.rooms:
            if room.room_type == 'L' and room.room_occupants < 4:
                available_living_spaces.append(room)

        if new_person.job_group.upper() == 'FELLOW' and new_person.want_accomodation == 'Y':
            if not available_living_spaces:
                Amity.unallocated.append(new_person)
                print('No Living Spaces available. Person added to unallocated.')
                new_person.assigned_living_space = 'NULL'
                return False

            new_person.assigned_living_space = random.choice(
                available_living_spaces).room_name

            for room in Amity.rooms:
                if room.room_name == new_person.assigned_living_space:
                    room.room_occupants += 1
            print(new_person.first_name + ' ' + new_person.last_name +
                  ' has been added to ' + new_person.assigned_living_space)
            return True

        else:
            new_person.assigned_living_space = 'NULL'

    def create_room(self, room_name, room_type):
        """Creates a new room in Amity."""
        if room_type.upper() not in ['O', 'L']:
            print('Invalid room type. Use: O for office or L for Livingspace')
            return False

        for room in Amity.rooms:
            if room.room_name == room_name.upper():
                print('A room with this name already exists.')
                return False

        new_room = Room()
        new_room.room_name = room_name.upper()
        new_room.room_type = room_type.upper()
        new_room.room_occupants = 0
        Amity.rooms.append(new_room)
        print('New room has been created.')
        return True

    def load_people(self, txt_file):
        """Adds people to rooms in Amity from a text file."""
        try:
            with open(txt_file) as file:
                for line in file.readlines():
                    person = line.replace('\n', '').split()
                    self.add_person(*person)

        except FileNotFoundError:
            print("It seems that file doesn't exist.")
            return False

    def print_room(self, room_name):
        """Prints names of all the people inside room_name"""
        room_members = []
        all_rooms = [room.room_name for room in Amity.rooms]
        if room_name.upper() not in all_rooms:
            print("Room doesn't exist")
            return False
        for person in Amity.persons:
            if person.assigned_living_space == room_name.upper(
            ) or person.assigned_office == room_name.upper():
                room_members.append(person)
        print('\nMembers of %s' % room_name.upper() + '\n' + '-' * 30)
        if len(room_members) == 0:
            print('There is no one in this room.')
            return False
        for member in room_members:
            full_name = member.first_name + ' ' + member.last_name
            print(full_name)
            return True

    def print_allocations(self, file_name=None):
        """Prints a list of allocations onto screen or text file specified."""
        if not Amity.rooms:
            print('There are currently no existing rooms in Amity.')
        else:
            rooms_list = [room.room_name for room in Amity.rooms]
            for room in rooms_list:
                members = [person.first_name + " " + person.last_name
                           for person in Amity.persons
                           if person.assigned_office == room
                           or person.assigned_living_space == room]
                print('\n' + room + '\n' + '-' * 30)
                if len(members) == 0:
                    print('There is no one in this room.\n')
                for member in members:
                    print(member)
                if file_name:
                    file = open(file_name + '.txt', 'a')
                    file.write('\n' + room + '\n' + '-' * 30 + '\n')
                    for member in members:
                        file.write(member + '\n')
                        file.close

    def reallocate_person(self, person_last_name, room_name, room_type):
        """Reallocate the person with person_identifier to new_room_name."""
        offices = []
        living_spaces = []
        room_name = room_name.upper()
        for room in Amity.rooms:
            if room.room_type.upper() == 'O' and room.room_occupants < 6:
                offices.append(room)
            elif room.room_type.upper() == 'L' and room.room_occupants < 4:
                living_spaces.append(room)

        # Checking person's existence
        if person_last_name.upper() in \
                [person.last_name for person in Amity.persons]:
            # Checking room's existence
            if room_name in [room.room_name for room in Amity.rooms]:
                # Checking if person is already in the room
                for person in Amity.persons:
                    if (person.last_name == person_last_name):
                        break

                # Check that person is not moving from office to living space
                # and vice versa
                if person.assigned_office != room_name:
                    if room_type.upper() == 'O':
                        if room_name in [
                                office.room_name for office in offices]:
                            person.assigned_office = room_name
                            print(person.first_name + person.last_name
                                  + ' has been reallocated to ' + room_name)
                        else:
                            print(person.last_name +
                                  ' cannot move from office to Living space.')
                            return 'Failed.'
                else:
                    print('Person is already there!')
                    return 'Failed.'

                if person.assigned_living_space != room_name and person.job_group == 'FELLOW':
                    if room_type.upper() == 'L':
                        if room_name in [
                                living_space.room_name for living_space in living_spaces]:
                            person.assigned_living_space = room_name
                            print(person.first_name + person.last_name
                                  + ' has been reallocated to ' + room_name)
                        else:
                            print(person.last_name +
                                  ' cannot move from Living space to office.')
                            return 'Failed.'
                    for room in Amity.rooms:
                        if room.room_name == room_name:
                            room.room_occupants += 1
                else:
                    print("Person is already there, or person is Staff.")
                    return 'Failed.'
            else:
                print("Room does not exist")
        else:
            print("Person does not exist")

    def print_unallocated(self, file_name=''):
        """Prints a list of unallocated people to the screen or specified file_name."""
        no_office = [person.first_name + ' ' + person.last_name
                     for person in Amity.unallocated
                     if person.assigned_office == 'NULL']
        no_living_space = [person.first_name + ' ' + person.last_name
                           for person in Amity.unallocated
                           if person.assigned_living_space == 'NULL' and person.job_group == 'FELLOW']

        print('\nPeople without Offices:' + '\n' + '-' * 30)
        if not len(no_office):
            print('No unallocated people.\n')
        for person in no_office:
            print(person)

        print('\nPeople without Living Spaces:' + '\n' + '-' * 30)
        if not len(no_living_space):
            print('No unallocated people.\n')
        for person in no_living_space:
            print(person)

        if file_name:
            file = open(file_name + '.txt', 'a')
            file.write('\nPeople without Offices:\n' + '-' * 30 + '\n')
            if not len(no_office):
                file.write('No unallocated people.\n')
            for person in no_office:
                file.write(person + '\n')
            file.write('\nPeople without Living Spaces:\n' + '-' * 30 + '\n')
            if not len(no_living_space):
                file.write('No unallocated people.\n')
            for persons in no_living_space:
                file.write(person + '\n')

    def save_state(self, db='alloamity_db.sqlite'):
        """Persists all data stored in application to database."""
        for room in Amity.rooms:
            room_to_save = Room(
                room_name=room.room_name,
                room_type=room.room_type,
                room_occupants=room.room_occupants
            )

            session.merge(room_to_save)

        for person in Amity.persons:
            person_to_save = PersonModel(
                first_name=person.first_name,
                last_name=person.last_name,
                job_group=person.job_group,
                want_accomodation=person.want_accomodation,
                assigned_office=person.assigned_office,
                assigned_living_space=person.assigned_living_space
            )

            session.merge(person_to_save)

        if not os.path.exists('alloamity_db.sqlite'):
            Session().create_database()
            session.commit()
            print('Stored to default db alloamity_db.sqlite.')
            return True
        else:
            Session().create_database(db)
            session.commit()
            print('Stored to' + db + ' .')
            return True
