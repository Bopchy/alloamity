from models.amity_database import *


class Amity(object):
	"""
	Class that print allocations of persons within amity, as well as
	unallocated fellows 
	"""
	def __init__(self):
		self.rooms, self.persons = self.load_state()

	def load_state(self, db_name='cp1.db'):
		def rooms():
			return DC.session.query(Room)
		def persons():
			return DC.session.query(Person)

		return (rooms(), persons(),)  
 
	def print_allocations(self):
		existing_rooms = self.rooms.all()
		if len(existing_rooms) == 0:
			print('No one has been allocated a room.')
		for room in existing_rooms:
			if room.room_type == 'Office':
				members_of_the_room = self.persons.filter_by(assigned_office=room.room_name).all()
				print(room.room_name)
				print('-' * 30)
				if len (members_of_the_room) == 0:
					print('This room is empty')
				member_names = [member.first_name + ' ' + member.last_name for member in members_of_the_room]
				print(', '.join(member_names) + '\n')

			else:
				members_of_the_room = self.persons.filter_by(assigned_living_space=room.room_name).all()
				print(room.room_name)
				print('-' * 30)
				if len (members_of_the_room) == 0:
					print('This room is empty')
				member_names = [member.first_name + ' ' + member.last_name for member in members_of_the_room]
				print(', '.join(member_names) + '\n')
		 
	def print_unallocated(self): # Prints fellows that said N to want_accomodation  
		unallocated = self.persons.filter_by(want_accomodation='N').all()
		if len(unallocated) == 0:
			print('There are currently no unallocated fellows.')
			return
		
		unallocated_fellows = [fellow.first_name + ' ' + fellow.last_name for fellow in unallocated]

		for fellow in unallocated_fellows:
			print(fellow)

	@staticmethod
	def save_state():
		DC.session.commit()


######### Print list of all the fellows in Amity
######### Print all the living spaces in Amity
######### Print all offices
############## Print a list of all the staff members in Amity 



	
# a1 = Amity()
# a1.print_unallocated() 
# Amity.print_unallocated()
# data = Amity.load_state(db)
# narnias = (data['Persons'].filter_by(assigned_office='Narnia').all())
# [print(narnia.first_name) for narnia in narnias]
# # print(data)