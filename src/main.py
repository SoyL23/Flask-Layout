from config.db import *
from models.user_model import User

class Main:

    def __init__(self):
        
        self.create_tables()

    def create_tables(self):
        
        Base.metadata.create_all(db.engine)
        print("Database is connect!")

if __name__ == '__main__':
    main = Main()
