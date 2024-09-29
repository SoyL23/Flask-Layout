from flask import Blueprint, jsonify, make_response, request
from interfaces.route_base import Route
from controllers.user_controller import user_controller

user_bp: Blueprint = Blueprint("user", __name__, url_prefix="/users")

class UserRoutes(Route):

    @staticmethod
    @user_bp.route("/create", methods=["POST"])
    def post():
        if request.method == "POST":
            return user_controller.create()
        else:
            return make_response(jsonify( {"message": "Method Not Allowed"} ), 404)

    @staticmethod
    @user_bp.route("/<id>")
    def get(id:int):
        if request.method == "GET":
            return user_controller.get_one(id)

    @staticmethod
    @user_bp.route("/list")
    def get_list():
        if request.method == "GET":
            return user_controller.get_all()
        else:
            return make_response(jsonify( {"message": "Method Not Allowed"} ), 404)

    @staticmethod
    @user_bp.route("/<id>", methods=["PUT"])
    def put(id:int):
        if request.method == "PUT":
            return user_controller.edit(id)

    @staticmethod
    @user_bp.route("/<id>", methods=["DELETE"])
    def delete(id:int):
        if request.method == "DELETE":
            return user_controller.remove(id)
