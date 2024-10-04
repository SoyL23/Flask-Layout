import os
from dotenv import load_dotenv

class Config:

    #Esta clase crea el String que se usa como motor de consultas SQL
    load_dotenv()
    
    def __init__(self):

        self.__user:str = os.getenv('DB_USER')
        self.__password:str = os.getenv('DB_PASSWORD')  
        self.__host:str = os.getenv('DB_HOST')
        self.__db:str = os.getenv('DB_NAME')
        self.__db_driver:str = os.getenv("DB_DRIVER")
        self.SECRET_KEY:str = os.getenv("SECRET_KEY")
        
        # print(self.__db_driver)

    
    @property
    def async_engine(self) -> str:
        return f'{self.__db_driver}://{self.__user}:{self.__password}@{self.__host}/{self.__db}'

class ConfigDev(Config): 
    PORT = 5000
    DEBUG = True
    LOAD_DOTENV = True
    TESTING = True
    
    def __init__(self):
        super().__init__()
        self.DATABASE_URI = self.async_engine

        

class ConfigProd(Config):
    PORT = 8080
    DEBUG = False
    LOAD_DOTENV = True
    TESTING = False
    
    
    def __init__(self):
        super().__init__()
        self.DATABASE_URI = self.async_engine
    