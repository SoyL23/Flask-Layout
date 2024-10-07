from flask import request
from models.user_model import User
from flask_jwt_extended import create_access_token
from models.auth_logs import LogEvents
from dto.auth_dto import AuthDTO
from services.user_service import UserService
from services.auth_log_services import AuthLogServices


class AuthService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def generate_token(user: User):
        return create_access_token(
            str(user.username), additional_claims={"type": "authorization"}
        )

    # @staticmethod
    # def get_auth_data() -> tuple:
    #     data: dict = request.get_json()
    #     username = data.get("username")
    #     password = data.get("password")
    #     data["ip"] = request.remote_addr
    #     data["event"] = LogEvents.LOGIN
    #     data.pop("username")
    #     data.pop("password")
    #     return username, password, data
    
    @staticmethod
    def get_auth_data() -> AuthDTO:
        data: dict = request.get_json()
        username = data.get("username")
        password = data.get("password")
        
        if not username or not password:
            raise ValueError("Username and password are required")
        
        return AuthDTO(username=username, password=password)
    
    async def validate_user(auth_dto: AuthDTO, data: dict ) -> tuple:
        user = await UserService.get_user_by_username(auth_dto.username) or False
        if user and isinstance(user, User) and user.check_password(auth_dto.password):
            data["success"] = True
            data["user_id"] = user.id
            return user, data
        else:
            data["success"] = False
            data["user_id"] = None
            return False, data
        
        
    async def login_user(auth_dto: AuthDTO) -> tuple:
        data = {
            'ip': request.remote_addr,
            'event': LogEvents.LOGIN
        }
        
        user, data = await AuthService.validate_user(auth_dto, data)
        if not user:
            await AuthLogServices.create(data=data)
            return {'message':'User not found'}, 401
        token = AuthService.generate_token(user)
        await AuthLogServices.create(data=data)
        return {'token': token}, 200
    # def login(self, username, password,) -> str:
        
