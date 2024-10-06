from flask import Flask, jsonify, request
from models.user_model import User
from flask_jwt_extended import create_access_token 

class AuthService:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def generate_token(self, user: User):
        return create_access_token(user.role)
                                   
    