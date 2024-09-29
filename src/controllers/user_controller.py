from services.user_service import user_service
from interfaces.controller_base import Controller
from flask import jsonify, make_response, request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from typing import List
from dto.user_dto import UserDTO

class UserController(Controller):
     
    @staticmethod
    def create():
        try:
            data: UserDTO = UserDTO(**request.get_json())
            response = user_service.create(data)

            if isinstance(response, dict):
                return make_response(jsonify(response), 201)
            
            if isinstance(response, IntegrityError):
                print(f"Error: {response}")
                return make_response(jsonify({"message":"Username has been used" }))
            
            if isinstance(response, SQLAlchemyError):
                print(f"Database Error: {response}")
                return make_response(jsonify({"message": "Database Error"}), 500)
            
        except Exception as e:
            print(f"Error: {e}")
            return make_response(jsonify( {"message":"An error has occurred"} ), 500)

    @staticmethod
    def get_one(user_id:int):
        try:

            response = user_service.read_one(user_id)

            if isinstance(response, dict):
                return make_response(jsonify(response), 200)
            
            if isinstance(response, SQLAlchemyError):
                print(f"Database Error: {e}")
                return make_response(jsonify({"message": "Database Error"}), 500)
            
            return make_response(jsonify({"message": "User not found"}), 404)
        
        except Exception as e:
            print(f"Error: {e}")
            return make_response(jsonify( {"message":"An error has occurred"} ), 500)
        

    @staticmethod
    def get_all():
        try:
            response = user_service.read_all()

            if isinstance(response, List) and len(response) > 0:
                return make_response(jsonify(response), 200)
            
            if isinstance(response, SQLAlchemyError):
                print(f"Database Error: {response}")
                return make_response(jsonify({"message": "Database Error"}), 500)
            
            return make_response(jsonify({"message": "Users is Empty"}), 200)
        except Exception as e:
            print(f"Error: {e}")
            return make_response(jsonify( {"message":"An error has occurred"} ), 500)
        

    @staticmethod
    def edit(user_id:int):
        try:
            data: dict = request.get_json()
            response = user_service.update(user_id, data)

            if isinstance(response, dict):
                return make_response(jsonify(response), 200)
            
            if isinstance(response, IntegrityError):
                print(f"Error: {response}")
                return make_response(jsonify({"message":"Username has been used" }))
            
            if isinstance(response, SQLAlchemyError):
                print(f"Database Error: {e}")
                return make_response(jsonify({"message": "Database Error"}), 500)
            
            return make_response(jsonify({"message": "User not found"}), 404)

        except Exception as e:
            print(f"Error: {e}")
            return make_response(jsonify( {"message":"An error has occurred"} ), 500)
        

    @staticmethod
    def remove(user_id:int):
        try:
            response = user_service.delete(user_id)

            if response:
                return make_response(jsonify({"message": "User deleted successfully"}), 200)
            
            if isinstance(response, SQLAlchemyError):
                print(f"Database Error: {e}")
                return make_response(jsonify({"message": "Database Error"}), 500)
            
            return make_response(jsonify({"message": "User not found"}), 404)
        
        except Exception as e:
            print(f"Error: {e}")
            return make_response(jsonify( {"message":"An error has occurred"} ), 500)
        
user_controller = UserController()
