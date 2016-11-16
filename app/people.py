class Person(object):

    """Class Person()"""

    def __init__(self, person_id, first_name, last_name, job_group, want_accomodation="N"):
        self.person_id = person_id
        self.full_name = first_name + " " + last_name
        self.job_group = job_group
        self.want_accomodation = want_accomodation
