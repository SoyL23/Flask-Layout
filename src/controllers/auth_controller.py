from services.user_service import UserService
from models.user_model import User
from flask import jsonify
from services.auth_service import AuthService
from services.auth_log_services import AuthLogServices
from dto.auth_dto import AuthDTO


class AuthController:

    # def __init__(self) -> None:
    #     pass

    # @staticmethod
    # async def validate_register(username: str, data: dict):
    #     user = await UserService.get_user_by_username(username) or False

    #     if user == False:
    #         data["success"] = user
    #         data["user_id"] = None

    #     elif isinstance(user, User):
    #         data["success"] = True
    #         data["user_id"] = user.id
    #     return user, data

    # @staticmethod
    # async def login():
    #     try:
    #         username, password, data = AuthService.get_auth_data()
    #         user, data = await AuthController.validate_register(
    #             username=username, data=data
    #         )
    #         if user == False:
    #             log = AuthLogServices.create(data=data)
    #             print(log)
    #             return jsonify({"message": "User not found"}), 401
    #         elif isinstance(user, User) and user.check_password(password):
    #             token = AuthService.generate_token(user=user)
    #             log = await AuthLogServices.create(data=data)
    #             print(log)
    #             return jsonify({"token": token})
    #         else:
    #             return jsonify({"error: {user}"})

    #     except Exception as e:
    #         print(f"Error: {e}")

    @staticmethod
    async def login():
        try:
            auth_dto: AuthDTO = AuthService.get_auth_data()
            
            response, status_code = await AuthService.login_user(auth_dto)
            
            return jsonify(response), status_code
        
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": "Internal server error"}), 500