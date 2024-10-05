from app import app
from config.config import ConfigDev

class Index:
    def __init__(self) -> None:
        app.logger.info(f"*"*40)
        app.logger.info(f"* APPLICATION IS RUNNING IN PORT: {ConfigDev.PORT} *")
        app.logger.info(f"*"*40)
