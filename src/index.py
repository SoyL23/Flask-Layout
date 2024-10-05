from app import app
from main import Main
from config.config import ConfigDev

class Index:
    def __init__(self) -> None:
        main = Main()
        app.logger.info(f"*"*40)
        app.logger.info(f"* APPLICATION IS RUNNING IN PORT: {ConfigDev.PORT} *")
        app.logger.info(f"*"*40)
        



    
index = Index()