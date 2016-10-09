from ..models.amity_database import Room, sess

class Room(object):
    """ Class that can create rooms, randomly add people to rooms,
        check rooms for available space 
    """
    def __init__(self):
        self.session = sess
    	

    def create_room(self, room_name, room_type, room_capacity):
    	new_room = Room()
        new_room.room_name = room_name
        new_room.room_type = room_type
        new_room.room_capacity = room_capacity
        sess.add(new_room)
        sess.commit(new_room)

    def space_available():
    	

    def add_person(self, person_id, room_name):
    	pass

    def reallocate_person():
    	pass