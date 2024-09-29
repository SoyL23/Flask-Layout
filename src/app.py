from flask import Flask
from routes.user_routes import user_bp

class App(Flask):
    pass

app = App(__name__)

@app.route("/")
def home():
    print("Server is online")
    return "Server is online"


app.register_blueprint(user_bp)