from .room import Room


class LivingSpace(Room):

    """docstring for LivingSpace"""

    def __init__(self, new_person):
        pass

    # def add_person_to_living_space(self, new_person):
    #     the_living = []
    #     self.list_of_living_spaces = rooms.filter_by(room_type='L').all()

    #     for living_space in self.list_of_living_spaces:
    #         is_there_living_space = self.space_available(
    #             living_space.room_name)
    #         if is_there_living_space:
    #             the_living.append(living_space)

    #     new_person.assigned_living_space = random.choice(
    #         self.list_of_living_spaces).room_name
    #     rooms.filter_by(room_name=new_person.assigned_living_space)\
    #         .update({'room_occupants': RoomModel.room_occupants+1})
