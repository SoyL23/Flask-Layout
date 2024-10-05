from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import Config, ConfigDev

class Database:
    
    #Esta clase crea un objeto Database con motor para consultas SQL
    #Ademas, incluye un atributo session el cual permite hacer consultas 

    def __init__(self, config:Config):
        
        self.engine = create_async_engine(config.async_engine)
        self.__Session = sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )
        self.session = self.__crear_sesion()

    def __crear_sesion(self):
        return self.__Session()

Base = declarative_base()

config = Config()

db = Database(config)

print("engine: ",db.engine)