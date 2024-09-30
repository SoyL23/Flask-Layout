from flask import Flask
from routes.user_routes import user_bp
from config.config import *

class App(Flask):
    pass

app = App(__name__)

@app.route("/")
def home():
    return "Server is online"

app.config.from_object(ConfigDev)
app.register_blueprint(user_bp)