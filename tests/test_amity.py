import os
import unittest
from app.amity import Amity
from app.livingspace import LivingSpace
from app.office import Office
from app.people import Person
from models.session import Session


class TestAmity(unittest.TestCase):

    """Tests Class Amity"""

    def setUp(self):
        self.amity = Amity()
        all_rooms = [
            ('Narnia', 'O'),
            ('Shire', 'O'),
            ('Python', 'L'),
            ('Javascript', 'L')
        ]
        all_people = [
            ('ROSY', 'BROWN', 'STAFF'),
            ('BREVER', 'POLAS', 'FELLOW', 'Y'),
            ('KHADIJA', 'MALUM', 'FELLOW')
        ]

    def tests_amity_system_initializes_with_nothing(self):
        self.assertEqual(len(self.amity.rooms), 0)
        self.assertEqual(len(self.amity.persons), 0)
        # check there is no database connection as well

    def tests_if_amity_creates_rooms(self):
        """Tests amity creates a room object, and stores
        the room object in a tuple called rooms()"""

        self.assertEqual(len(self.amity.rooms), 0)
        self.amity.create_room('Krypton', 'O')
        self.assertIn(('Krypton', 'O'), self.amity.rooms)

        self.amity.create_room('Ruby', 'L')
        self.assertIn(('Ruby', 'L'), self.amity.rooms)

    def tests_if_amity_checks_space_available(self):
        livingspace = self.amity.create_room('Python', 'L')
        LivingSpace.room_occupants = 2
        livingspace_room_capacity = LivingSpace.room_capacity
        self.assertEqual(livingspace_room_capacity, 4)
        self.assertTrue(self.amity.space_available(livingspace))

        office = self.amity.create_room('Topaz', 'O')
        Office.room_occupants = 4
        office_room_capacity = Office.room_capacity
        self.assertEqual(office_room_capacity, 6)
        self.assertFalse(self.amity.space_available(office))

    def tests_if_amity_adds_person(self):
        self.amity.add_person('Rose', 'Flowers', 'Staff')
        self.amity.add_person('Benny', 'Flinn', 'Fellow', 'Y')
        self.assertIn(('Benny', 'Flinn', 'Fellow', 'Y'), Amity.persons)
        self.assertIn(('Rose', 'Flowers', 'Staff'), Amity.persons)
        self.assertEqual(len(Amity.persons), 2)
        # Asserts that not more people than specified have been added

    def test_amity_prints_allocations_to_text_file(self):
        self.amity.print_allocations({'--o': 'test_allocations.txt'})
        self.assertTrue(os.path.exists('test_allocations.txt'))
        file_name_open = open('test_allocations.txt')
        while file_name_open:
            line = f.readline()
            self.assertIn(('ROSA PARKS FELLOW Y'), line)
        os.remove('test_allocations.txt')

    def tests_amity_prints_unallocated_to_text_file(self):
        self.amity.add_person('Peter', 'Wright', 'Fellow')
        self.amity.print_unallocated({'--o': 'test_unallocated.txt'})
        self.assertTrue(os.path.exists('test_unallocated.txt'))
        file_name_open = open('test_unallocated.txt')
        while file_name_open:
            line = file_name_open.readline()
            self.assertIn('PETER WRIGHT FELLOW', line)
        os.remove('test_unallocated.txt')

    def tests_amity_loads_people(self):
        self.amity.persons = []
        self.amity.load_people(os.path.dirname(__file__))
        self.assertIn(('RACHEL', 'SPARKS', 'STAFF'), self.amity.persons)

    def tests_amity_reallocates_persons(self):
        room = self.amity.create_room('Hogspush', 'O')
        person = self.amity.add_person('Stella', 'Marks', 'Staff')
        person.person_id = 1
        self.assertIn(person, room)
        room_2 = self.amity.create_room('Stardom', 'O')
        self.amity.reallocate_person(person.person_id, room_2)
        self.assertIn(person, room_2)

    def tests_amity_loads_state(self):
        pass

    def tests_amity_saves_state(self):
        pass

    def tearDown(self):
        self.amity = None

if __name__ == '__main__':
    unittest.main()
