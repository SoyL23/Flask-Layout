from config.db import Base
from sqlalchemy import Column, Integer, String, DateTime, func, Enum
from werkzeug.security import generate_password_hash, check_password_hash
import enum

class Role(enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    GUEST = "GUEST"


class User(Base):

    __tablename__ = "Users"
    
    id = Column(Integer(), primary_key=True, autoincrement=True, name='User_id')
    username = Column(String(12), nullable=False, unique=True, name="Username")
    password = Column(String(255), nullable=False, name="Password")
    role = Column(Enum(Role), nullable=False, name="User_role")
    CREATED_AT = Column(DateTime, nullable=False, server_default=func.now(), onupdate=None)


    def set_password(self, password):
        return generate_password_hash(password)
    
    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)

    def to_dict(self):
        return{
            'id':self.id,
            'username': self.username,
            'password': self.password,
            'role': f'{self.role}' ,
            'created_at': self.CREATED_AT

        }
