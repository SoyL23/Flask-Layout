from flask import Flask, jsonify, request
from models.user_model import User
from flask_jwt_extended import create_access_token 

class AuthService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod    
    def generate_token(user: User):
        return create_access_token(str(user.role), additional_claims={'type':'authorization'})
                                   
    