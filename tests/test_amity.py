from app.amity import Amity  

import unittest
from unittest.mock import MagicMock, patch

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

	@patch('test_amity.load_state')
	def tests_amity_loads_state(self, mock_load_state):
		pass	

	def tests_amity_saves_state(self):
		pass
