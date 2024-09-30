from config.db import *
from models.user_model import User
from app import app

class Main:

    def __init__(self):
        self.create_tables()
        app.logger.info(f"*"*40)
        app.logger.info(f"*      ALL MODELS HAS BEEN CREATED     *")
        app.logger.info(f"*"*40)
        

    def create_tables(self):
        app.logger.warning(f"*"*40)
        app.logger.warning(f"*       CONNECTING TO DATABASE...      *")
        app.logger.warning(f"*"*40)
        Base.metadata.create_all(db.engine)
    
        
        

# if __name__ == '__main__':
#     main = Main()
