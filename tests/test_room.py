import unittest
import mock
from app.room import Room
from app.people import Person
from tests.test_database import CreateTestDatabase


class TestRoom(unittest.TestCase):

    """docstring for TestRoom
    """

    def setUp(self):
        """ Sets up test data
        """
        self.room = Room()
        # self.office_max = 6
        # self.livingspace_max = 4
        self.new_person = Person()

    def tests_rooms_check_for_available_space(self):
        pass

    def tests_room_adds_person(self):

        self.room.add_person(self.new_person)
        self.assertIn(self.new_person, new_office)

    def tests_room_reallocates_person(self):
        pass
