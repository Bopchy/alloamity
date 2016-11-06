from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session(object):

    def __init__(self, db_name=None):
        self.db_name = db_name
        if self.db_name:
            self.engine = create_engine('sqlite:////' + self.db_name + '.sqlite')
            print('Your database' + db_name + ' has been created')

        else:
            self.engine = create_engine('sqlite:////alloamity_db.sqlite')

    def create_session(self):
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        return self.session

    def create_database(self, db_name='alloamity_db.sqlite'):
        sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
        return true
