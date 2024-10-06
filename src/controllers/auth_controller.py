from services.user_service import UserService
from models.user_model import User
from flask import jsonify
from services.auth_service import AuthService

class AuthController:
    
    def __init__(self) -> None:
        pass
    
    
    @staticmethod
    async def validate_register(username: str):
        return await UserService.get_user_by_username(username) or False
    
    @staticmethod
    async def login(data:dict):
        try:
            username = data.get("username")
            password = data.get("password")
            user: User = await AuthController.validate_register(username)
            if user == False:
                return jsonify({"message":"User not found"}),401
            elif isinstance (user, User) and user.check_password(password):
                token = AuthService.generate_token(user=user)
                print(token)
                return token
            
        except Exception as e:
            pass 
            
        
        