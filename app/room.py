class Room(object):

    """Class Room()."""

    def __init__(self, room_name, room_type, room_occupants):
        self.room_name = room_name.upper()
        self.room_type = room_type.upper()
        self.room_occupants = room_occupants
