""" AlloAmity is an Office Space allocation sysytem that allocates 
	offices and living sapces in Amity, one of Andela's facilties.   

Usage: 
		amity 	create_room <room_name> <room_type> <room_capacity>
		amity 	add_person <person_name> <FELLOW|STAFF> [want_accommodation]
		amity 	reallocate_person <person_identifier> <new_room_name>
		amity 	load_people
		amity 	print_allocations [-o=filename]
		amity 	print_unallocated [-o=filename]
		amity 	print_room <room_name>
		amity 	save_state [--db=database]
		amity 	load_state <database> 
		amity 	--help|-h
		amity 	--version
		amity 	--interactive|-i

Options: 
		-o 			outputs to a file with specified filename
		--db 		specifies the database that should be saved to 
		--help,-h 	shows this help message and exits
		--version	shows the version of AlloAmity
		--interactive, -i 	interactive mode 

"""

import sys
import cmd
from amity import amity, room, people
from docopt import docopt, DocoptExit 

def docopt_cmd(func):

    def fn(self, arg):
    	try:
    		opt = docopt(fn.__doc__, arg)
    	except DocoptExit as e:
    		print('Invalid Command!')
    		print(e)
    		return 
    	except SystemExit:
    		return

    	return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)

    return fn

class AlloAmity(cmd.Cmd):
	
	intro = 'Welcome to AlloAmity - A Space allocation system \n\n' 
	prompt = 'AlloAmity-->'

	@docopt_cmd
	def do_create(self, args):
		''' 
		Creates new rooms in Amity 

		Usage: create_room <room_name> <room_type> <room_capacity>

		'''
		room.Room.create_room(args["<room_name>"], args["<room_type>"], args["<room_capacity>"])

	
	def save_state():
		'''
		Persists user session into the database
		'''
		save_state()



if __name__ == '__main__':
	AlloAmity().cmdloop()



