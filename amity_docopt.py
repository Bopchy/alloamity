"""
AlloAmity is an Office Space allocation sysytem that allocates
offices and living sapces in Amity, one of Andela's facilties.

Usage:
    amity   create_room <room_name> <room_type>
    amity   add_person <first_name> [--last_name='no'] <job_group> [--want_accomodation='N']
    amity   reallocate_person <person_last_name> <room_name> <room_type>
    amity   load_people <txt_file>
    amity   print_allocations [--o=file_name]
    amity   print_unallocated [--o=file_name]
    amity   print_room <room_name>
    amity   save_state [--db=database]
    amity   load_state <database>
    amity   help

Options:
    -o          outputs to a file with specified filename
    --db        specifies the database that should be saved to

"""

import cmd
from docopt import docopt, DocoptExit

from app.amity import Amity
from models.amity_database import Session


session = Session().create_session()
a = Amity(session)


def docopt_cmd(func):

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            print('\nInvalid Command! Type help to see list of available commands')
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

    intro = '\nWelcome to AlloAmity - A Space allocation system \n'
    prompt = '(AlloAmity) $ '

    @docopt_cmd
    def do_about(self, args):
        """Displays the Usage docstring

        Usage: about"""
        print(__doc__)

    @docopt_cmd
    def do_create_room(self, args):
        """Creates new rooms in Amity

        Usage: create <room_name> <room_type> """
        a.create_room(args["<room_name>"], args["<room_type>"])

    @docopt_cmd
    def do_add_person(self, args):
        """Adds a person to the system and allocates the person to a random room.

        Usage: add_person <first_name> <last_name> <job_group> [--want_accomodation=N]"""
        want_accomodation = args['--want_accomodation']
        if want_accomodation is None:
            want_accomodation = 'N'

        a.add_person(
            args['<first_name>'],
            args['<last_name>'],
            args['<job_group>'],
            want_accomodation
        )

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Reallocate the person with person_last_name to the new_room.

        Usage: reallocate_person <person_last_name> <room_name> <room_type>"""
        a.reallocate_person(
            args['<person_last_name>'],
            args['<room_name>'],
            args['<room_type>'])

    @docopt_cmd
    def do_load_people(self, args):
        """Adds people to rooms from a txt file. See Appendix 1A for text input format.

        Usage: load_people <txt_file>"""
        a.load_people(args['<txt_file>'])

    @docopt_cmd
    def do_print_allocations(self, args):
        """ Prints a list of allocations onto the screen. Specifying the
        optional -o option here outputs the registered allocations to a txt file.

        Usage: print_allocations [--o=file_name]"""
        a.print_allocations(args['--o'])

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Prints a list of unallocated people to the screen. Specifying the -o
        option here outputs the information to the txt file provided.

        Usage: print_unallocated [--o=file_name]"""
        a.print_unallocated(args['--o'])

    @docopt_cmd
    def do_print_room(self, arg):
        """Prints  the names of all the people in room_name on the screen.

        Usage: print_room <room_name>"""
        a.print_room(arg['<room_name>'])

    @docopt_cmd
    def do_load_state(self, args):
        """Loads data from a database into the application.

        Usage: load_state <sqlite_database>"""
        a.load_state(args['<sqlite_database>'])

    @docopt_cmd
    def do_save_state(self, args):
        """Persists user session into the database

        Usage: save_state [--db=database]"""
        a.save_state(args['--db'])

    @docopt_cmd
    def do_quit(self, arg):
        """Exits the application interface on the terminal

        Usage: quit"""
        print('\n********** You have exited AlloAmity **********\n')
        exit()


if __name__ == '__main__':
    AlloAmity().cmdloop()
