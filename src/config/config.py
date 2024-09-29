import os
from dotenv import load_dotenv
class Config:

    #Esta clase crea el String que se usa como motor de consultas SQL
    
    def __init__(self):

        load_dotenv()
        
        self.__user:str = os.getenv('DB_USER')
        self.__password:str = os.getenv('DB_PASSWORD')  
        self.__host:str = os.getenv('DB_HOST')
        self.__db:str = os.getenv('DB_NAME')
        self.__db_driver:str = os.getenv("DB_DRIVER")

    @property
    def engine(self) -> str:
        return f'{self.__db_driver}://{self.__user}:{self.__password}@{self.__host}/{self.__db}'

class ConfigDev(Config):
    pass

class ConfigProd(Config):
    pass