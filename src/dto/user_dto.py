from datetime import datetime

class UserDTO():
    
    def __init__(self, username: str = None, password: str = None, id: int = None, created_at = None) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.CREATED_AT = created_at
        
    def to_dict(self) -> dict:
        return{
            'id':self.id,
            'username': self.username,
            'password': self.password,
            'created_at': self.CREATED_AT
        }
        