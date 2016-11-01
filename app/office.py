from .room import Room


class Office(Room):

    """docstring for Office"""

    def __init__(self, args):
        # super(Office, self)
        passß

    # def add_person_to_office(self, new_person):
    #     the_offices = []
    #     self.list_of_offices = rooms.filter_by(room_type='O').all()

    #     for office in self.list_of_offices:
    #         is_there_office_space = super(Office, self).space_available(office.room_name)
    #         if is_there_office_space:
    #             the_offices.append(office)

    #     new_person.assigned_office = random.choice(the_offices).room_name
    #     # Is assigning an object from list of room objects query to
    #     # new_person.assigned_office

    #     rooms.filter_by(room_name=new_person.assigned_office)\
    #         .update({'room_occupants': Room.room_occupants+1})
