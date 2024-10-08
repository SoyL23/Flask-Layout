from flask import Flask, request
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from config.config import *
from flask_jwt_extended import JWTManager
from flask_cors import CORS


class App(Flask):
    pass


app = App(__name__)
app.config.from_object(ConfigDev)
CORS(app, supports_credentials=True)
jwt = JWTManager(app=app)


@app.route("/")
def home():
    return "Server is online"


app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)