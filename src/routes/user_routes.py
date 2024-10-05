from flask import Blueprint, jsonify, make_response, request
from interfaces.route_base import Route
from controllers.user_controller import USER_CONTROLLER

user_bp: Blueprint = Blueprint("user", __name__, url_prefix="/users")

class UserRoutes(Route):

    @staticmethod
    @user_bp.route("/create", methods=["POST"])
    async def post():
        return await USER_CONTROLLER.create()
        

    @staticmethod
    @user_bp.route("/<id>")
    async def get(id:int):
        if request.method == "GET":
            return await USER_CONTROLLER.get_one(id)

    @staticmethod
    @user_bp.route("/list")
    async def get_list():
        if request.method == "GET":
            return await USER_CONTROLLER.get_all()
        else:
            return make_response(jsonify( {"message": "Method Not Allowed"} ), 404)

    @staticmethod
    @user_bp.route("/<id>", methods=["PUT"])
    async def put(id:int):
        if request.method == "PUT":
            return await USER_CONTROLLER.edit(id)

    @staticmethod
    @user_bp.route("/<id>", methods=["DELETE"])
    async def delete(id:int):
        if request.method == "DELETE":
            return await USER_CONTROLLER.remove(id)

    @user_bp.route("/getcsv")
    async def get_users_csv():
        return await USER_CONTROLLER.users_csv()