from app.room import Room
from models.amity_database import Room as RoomModel


class Person(object):

    """ Class that loads people from a text file and randomly allocates them rooms,
        reallocates them from one room to another, exits people from a room.
    """

    def __init__(self, session):
        self.session = session

    @staticmethod
    def load_people(txt_file):
        file_name = txt_file
        with open(file_name) as file:
            for line in file.readlines():
                person = line.replace('\n', '').split()
                print(person)
                Room().add_person(*person)
                # Using python splat to add members of list as arguments to add_person()

    def reallocate_person(self, person_id, room_name):
        person_details = persons.filter_by(person_id=person_id).one()
        # person_job_group =
        room_details = rooms.filter_by(room_name=room_name).one()
        room_type = room_details.room_type
        space_status = Room().space_available(room_name)
        if space_status:
            if room_type == 'O':
                current_room = person_details.assigned_office
                persons.filter_by(person_id=person_id).update(
                    {'assigned_office': room_name})
                rooms.filter_by(room_name=room_name).update(
                    {'room_occupants': room_details.room_occupants+1})
                rooms.filter_by(room_name=current_room).update(
                    {'room_occupants': RoomModel.room_occupants-1})

            elif room_type == 'L':
                current_room = person_details.assigned_living_space
                persons.filter_by(person_id=person_id).update(
                    {'assigned_living_space': room_name})
                rooms.filter_by(room_name=room_name).update(
                    {'room_occupants': room_details.room_occupants+1})
                rooms.filter_by(room_name=current_room).update(
                    {'room_occupants': RoomModel.room_occupants-1})

    def exit_room(self, person_id, room_name):
        person_details = persons.filter_by(person_id=person_id).one()
        person_office_details = persons.filter(assigned_office)
        person_living_space_details = person_details.filter(assigned_living_space)
        try:
            if person_office_details is room_name:
                persons.filter_by(assigned_office=room_name).update({'assigned_office': 'NULL'})
            if person_living_space_details is room_name:
                persons.filter_by(assigned_living_space=room_name).update({'assigned_living_space': 'NULL'})
        except Exception:
            return 'Person' + person_id + 'is not in that room.'

# r = Person()
# r.reallocate_person('6', 'New')
# Person.load_people('input3')
