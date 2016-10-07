from amity.amity import Amity 
from amity.fellow import Fellow
from amity.livingspace import LivingSpace 
from amity.office import Office 
from amity.people import Person
from amity.room import Room 
from amity.staff import Staff

import unittest

class TestAmity(unittest.TestCase):
	"""Tests class Amity
	"""
	def setUp(self):
		
		pass

	def test_Amity_is_a_class(self):
		a = Amity()
		self.assertIsInstance(a, Amity)

	def test_amity_prints_allocations(self):
		pass

	def tests_amity_prints_unallocated(self):
		pass

	def tests_amity_loads_state(self):
		pass

	def tests_amity_saves_state(self):
		pass

class TestPerson(unittest.TestCase):
	""" 
	"""
	pass

	def tests_person_loads_people(self):
		pass

class TestRoom(unittest.TestCase):
	"""docstring for TestRoom
	"""
	def setUp(self):
		""" Sets up test data
		"""
		self.room = Room()
		self.office_max = 6
		self.livingspace_max = 4
		self.new_person = Person() 

	def tests_room_creates_new_rooms(self):
		"""Tests if a new office and Living Space are created 
		"""
		naruto = self.room.create_room("Naruto", "Office")
		# self.assertIsInstance(naruto, Office)

		self.assertEqual((1+1), 3)

		self.room.create_room("OnePiece", "LivingSpace")
		self.assertIsInstance("OnePiece", LivingSpace)

	def tests_rooms_check_for_available_space(self):
		""" Tests if available space is checked for
		"""
		pass

	def tests_room_adds_person(self):
		""" Tests if a new person is added to an office and living 
			space
		"""
		# new_office = 
		self.room.add_person(self.new_person)
		self.assertIn(self.new_person, new_office)

	def tests_room_reallocates_person(self):
		pass

	

