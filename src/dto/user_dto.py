from datetime import datetime
from models.user_model import Role

class UserDTO():
    
    def __init__(self, username: str, password: str, role:str, id:int = None, created_at= None) -> None:

        if id and created_at:
            self.id = id
            self.CREATED_AT = created_at

        if role == "ADMIN":
            role = Role.ADMIN
        elif role == "USER":
            role = Role.USER
        elif role == "GUEST":
            role = Role.GUEST
            
        self.role = role
        self.username = username
        self.password = password
        
    def to_dict(self) -> dict:
        return{
            # 'id': self.id if self.id else None,
            'username': self.username,
            'password': self.password,
            # 'created_at': self.CREATED_AT if self.CREATED_AT else None
            'role': self.role
        }
        