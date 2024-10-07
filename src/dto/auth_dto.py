

class AuthDTO:
    
    def __init__(self, username, password,):
        self.username = username
        self.password = password
        
    def to_dict(self) -> dict:   
        return {
            'username': self.username,
            'password': self.password
        }