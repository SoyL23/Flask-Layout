from flask import Blueprint, jsonify, make_response, request
from interfaces.route_base import Route
from controllers.user_controller import user_controller
from flask_jwt_extended import jwt_required

user_bp: Blueprint = Blueprint("user", __name__, url_prefix="/api/users")

class UserRoutes(Route):

    @staticmethod
    @user_bp.route("/create", methods=["POST"])
    async def post():
            return await user_controller.create()

    @staticmethod
    @user_bp.route("/<id>")
    @jwt_required()
    async def get(id:int):
        if request.method == "GET":
            return await user_controller.get_one(id)

    @staticmethod
    @user_bp.route("/list")
    @jwt_required()
    async def get_list():
        if request.method == "GET":
            return await user_controller.get_all()
        else:
            return make_response(jsonify( {"message": "Method Not Allowed"} ), 404)

    @staticmethod
    @user_bp.route("/<id>", methods=["PUT"])
    async def put(id:int):
        if request.method == "PUT":
            return await user_controller.edit(id)

    @staticmethod
    @user_bp.route("/<id>", methods=["DELETE"])
    async def delete(id:int):
        if request.method == "DELETE":
            return await user_controller.remove(id)

    @user_bp.route("/getcsv")
    async def get_users_csv():
        return await user_controller.users_csv()
    
   