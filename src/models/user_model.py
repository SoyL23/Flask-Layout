from config.db import Base
from sqlalchemy import Column, Integer, String, DateTime, func, Enum
import enum

class Role(enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    GUEST = "GUEST"


class User(Base):

    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, name='User_id')
    username = Column(String, nullable=False, unique=True, name="Username")
    password = Column(String, nullable=False, name="Password")
    role = Column(Enum(Role), nullable=False, name="User_role")
    CREATED_AT = Column(DateTime, nullable=False, server_default=func.now(), onupdate=None)



    def to_dict(self):
        return{
            'id':self.id,
            'username': self.username,
            'password': self.password,
            'role': f'{self.role}' ,
            'created_at': self.CREATED_AT

        }
