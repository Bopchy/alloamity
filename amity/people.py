from models.amity_database import sess, Person as PersonClass
from room import Room

class Person(object):
	"""docstring for People"""
	def __init__(self):
		pass

	@staticmethod
	def load_people(txt_file):
		pass

	def new_employee(self, first_name, last_name, job_group, want_accomodation, gender):
		new_person = PersonClass()
		new_person.first_name = first_name
		new_person.last_name = last_name
		new_person.job_group = job_group
		new_person.want_accomodation = want_accomodation
		new_person.gender = gender

		Room().add_person(new_person)

		sess.add(new_person)
		sess.commit()
	
# p1 = Person()
# p1.new_employee('Ruth', 'Bochere', 'Fellow', 'Y', 'F')