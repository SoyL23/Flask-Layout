from config.db import Base
from sqlalchemy import Column, Integer, String, DateTime, func

class User(Base):

    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, name='User_id')
    username = Column(String, nullable=False, unique=True, name="Username")
    password = Column(String, nullable=False, name="Password")
    CREATED_AT = Column(DateTime, nullable=False, server_default=func.now(), onupdate=None)

    def __init__(self, username: str, password: str, id: int = None, created_at = None):
        self.id = id
        self.username = username
        self.password = password
        self.CREATED_AT = created_at

    def to_dict(self):
        return{
            'id':self.id,
            'username': self.username,
            'password': self.password,
            'created_at': self.CREATED_AT
        }
