from services.user_service import UserService
from models.user_model import User
from flask import jsonify, request
from services.auth_service import AuthService

class AuthController:
    
    def __init__(self) -> None:
        pass
    
    
    @staticmethod
    async def validate_register(username: str):
        return await UserService.get_user_by_username(username) or False
    
    @staticmethod
    async def login():
        try:
            data:dict = request.get_json()
            username = data.get("username")
            password = data.get("password")
            user: User = await AuthController.validate_register(username)
            if user == False:
                return jsonify({"message":"User not found"}),401
            elif isinstance (user, User) and user.check_password(password):
                token = AuthService.generate_token(user=user)
                return jsonify({'token': token})
            else:
                return jsonify({'error: {user}'})
            
        except Exception as e:
            print(f"Error: {e}")
            
        
        