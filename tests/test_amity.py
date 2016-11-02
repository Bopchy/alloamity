import unittest
from app.amity import Amity
from app.amity import LivingSpace
from app.amity import Office
from models.session import Session

session = Session().create_session()


class TestAmity(unittest.TestCase):

    """Tests Class Amity"""

    def setUp(self):
        self.Amity = Amity(session)
        self.rooms = []
        self.people = []
        self.staff_members = [
            ('Ruth', 'Bochere', 'Fellow', 'Y', 'F'),
            ('Edward', 'Karanja', 'Fellow', 'N', 'M'),
            ('Peter', 'Yotti', 'Staff'),
            ('Whitney', 'Ruoroh', 'Staff'),
            ('Steve', 'Njoroh', 'Staff')
        ]

    def tests_amity_system_initializes_with_nothing(self):
        self.assertEqual(len(self.rooms), 0)
        self.assertEqual(len(self.people), 0)
        # check there is no database connection as well

    def tests_if_amity_creates_rooms(self):
        """Tests amity creates a room object, and stores the room object in a tuple called rooms()"""

        self.assertEqual(len(self.rooms), 0)
        self.Amity.create_room('Krypton', 'O')
        self.assertIn(('Krypton', 'O'), self.rooms)

        self.Amity.create_room('Ruby', 'L')
        self.assertIn(('Ruby', 'L'), self.rooms)

    def tests_if_amity_checks_space_available(self):
        livingspace_room_occupants = 2
        livingspace = self.Amity.create_room('Python', 'L')
        livingspace_room_capacity = LivingSpace.room_capacity
        self.assertEqual(livingspace_room_capacity, 6)
        self.assertTrue(self.Amity.space_available)

        office_room_occupants = 4
        office = self.Amity.create_room('Topaz', 'O')
        office_room_capacity = Office.room_capacity
        self.assertEqual(office_room_capacity, 4)
        self.assertFalse(self.Amity.space_available)

    def tests_if_amity_adds_person(self):
        self.assertEqual(len(self.people), 0)
        self.Amity.add_person('Bopchy', 'Beau', 'Fellow', 'Y', 'F')
        self.assertIn(('Bopchy', 'Beau', 'Fellow', 'Y', 'F'), self.people)

        self.Amity.add_person('Ruth', 'Bochere', 'Staff')
        self.assertIn(('Ruth', 'Bochere', 'Staff'), self.people)

    def tests_if_amity_adds_person_to_office(self):
        self.add_person

    def tests_if_amity_adds_person_to_living_space(self):
        pass

    def test_amity_prints_allocations(self):
        pass

    def tests_amity_prints_unallocated(self):
        pass

    def tests_amity_loads_state(self):
        pass

    def tests_amity_saves_state(self):
        pass
