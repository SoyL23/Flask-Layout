from flask import request
from models.user_model import User
from flask_jwt_extended import create_access_token
from models.auth_logs import LogEvents


class AuthService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def generate_token(user: User):
        return create_access_token(
            str(user.username), additional_claims={"type": "authorization"}
        )

    @staticmethod
    def get_auth_data() -> tuple:
        data: dict = request.get_json()
        username = data.get("username")
        password = data.get("password")
        data["ip"] = request.remote_addr
        data["event"] = LogEvents.LOGIN
        data.pop("username")
        data.pop("password")
        return username, password, data
