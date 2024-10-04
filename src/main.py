from config.db import *
from models.user_model import User
from app import app
import asyncio

class Main:

    def __init__(self):
        # Llamamos al método setup que maneja la asincronía
        asyncio.run(self.setup())

    async def setup(self):
        await self.create_tables()
        app.logger.info(f"*" * 40)
        app.logger.info(f"*      ALL MODELS HAVE BEEN CREATED     *")
        app.logger.info(f"*" * 40)
        

    async def create_tables(self):
        app.logger.warning(f"*"*40)
        app.logger.warning(f"*       CONNECTING TO DATABASE...      *")
        app.logger.warning(f"*"*40)
        
        async with db.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    
        
        

# if __name__ == '__main__':
#     main = Main()
