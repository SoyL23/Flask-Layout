from models.auth_logs import AuthLogs
from config.db import db


class AuthLogServices:

    @staticmethod
    async def create(data: dict) -> dict:
        try:
            log: AuthLogs = await AuthLogServices.__add_to_db(data)
            if log.id:
                return log.to_dict()
            return None
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    async def __add_to_db(data: dict):
        try:
            log: AuthLogs = AuthLogs(**data)
            db.session.add(log)
            db.session.commit()
            return log
        except Exception as e:
            print(f"Error: {e}")
