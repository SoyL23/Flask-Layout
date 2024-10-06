from flask import Flask
from routes.user_routes import user_bp
from config.config import *
from flask_jwt_extended import JWTManager, jwt_required

class App(Flask):
    pass

app = App(__name__)
app.config.from_object(ConfigDev)
jwt = JWTManager(app=app)


@app.route("/")
@jwt_required()
def home():
    return "Server is online"


app.register_blueprint(user_bp)

