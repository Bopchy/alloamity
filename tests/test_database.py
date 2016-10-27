import os
from models.amity_database import DatabaseCreate

DC = DatabaseCreate()

class CreateTestDatabase(object):
	test_db = DatabaseCreate('test_db')
	if os.path.exists('test_db.sqlite') and DC.session==None:
		os.remove('test_db.sqlite')
	pass