from models.amity_database import sess, Person as PersonClass
from room import Room

class Person(object):
	"""docstring for People"""
	def __init__(self):
		pass

	def load_people(self):
		pass

	def new_employee(self, first_name, last_name, job_group, want_accomodation, gender):
		new_person = PersonClass()
		new_person.first_name = first_name
		new_person.last_name = last_name
		new_person.job_group = job_group
		new_person.want_accomodation = want_accomodation
		new_person.gender = gender

		Room.add_person(new_person)

		sess.add(new_person)
		sess.commit()
	
p1 = Person()
p1.new_employee('Bopchy', 'Yea', 'Fellow', 'Y', 'F')
p2 = Person()
p2.new_employee('Bopchy', 'Iiii', 'Fellow', 'N', 'F')		
p4 = Person()
p4.new_employee('Bopchy', 'Got', 'Staff', 'N', 'F')				
p3 = Person()
p3.new_employee('Bopchy', 'This', 'Staff', 'N', 'F')	
