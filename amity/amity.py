from models.amity_database import Room, sess, Person

class Amity(object):
	"""C 
	"""
	def __init__(self):
		pass	

	# Using @staticmethod to avoid having to use the print_allocation()
	# with an instance of Amity class 
	@staticmethod 
	def print_allocations():
		existing_rooms = sess.query(Room).all()
		for room in existing_rooms:
			if room.room_type == 'Office':
				members_of_the_room = sess.query(Person).filter_by(assigned_office=room.room_name).all()
				print(room.room_name)
				print('-' * 30)
				member_names = [member.first_name + ' ' + member.last_name for member in members_of_the_room]
				print(', '.join(member_names) + '\n')

			else:
				members_of_the_room = sess.query(Person).filter_by(assigned_living_space=room.room_name).all()
				print(room.room_name)
				print('-' * 30)
				member_names = [member.first_name + ' ' + member.last_name for member in members_of_the_room]
				print(', '.join(member_names) + '\n')
		 
	@staticmethod
	def print_unallocated(): # Prints fellows that said N to want_accomodation  
		unallocated = sess.query(Person).filter_by(want_accomodation='N').all()

		if len(unallocated) == 0:
			print('There are currently no unallocated fellows.')
			return
		
		unallocated_fellows = [fellow.first_name + ' ' + fellow.last_name for fellow in unallocated]

		for fellow in unallocated_fellows:
			print(fellow)

	@staticmethod
	def load_state():
		pass

	@staticmethod
	def save_state():
		sess.commit()
	
# Amity.print_allocations() 
Amity.print_unallocated()
	

	

			
			

