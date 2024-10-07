from flask import Blueprint
from controllers.auth_controller import AuthController

auth_bp: Blueprint = Blueprint("auth_bp", __name__, url_prefix="/api/auth")

class AuthRoutes:
    

    @staticmethod
    @auth_bp.route("/login", methods=['POST'])
    async def login():
        return await AuthController.login()