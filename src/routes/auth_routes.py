from flask import Blueprint

auth_bp: Blueprint = Blueprint("auth_bp", __name__, url_prefix="/auth")

class AuthRoutes:
    pass
    