from app import app

class Index:
    def __init__(self) -> None:
        app.run(port=5000, debug=True)
    
index = Index()