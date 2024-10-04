from typing import List
from sqlalchemy.exc import SQLAlchemyError, IntegrityError 
from config.db import db, Database
from models.user_model import User
from dao.dao import DAO
from dto.user_dto import UserDTO
from utils.user_utils import UserUtils

class UserService(DAO):

    def __init__(self, db: Database, Model: User) -> None:
        super().__init__()
        self.Model = Model
        self.db = db
    
    async def create(self, userDTO: UserDTO) -> dict | IntegrityError | SQLAlchemyError:
        async with self.db.__crear_sesion() as session:
            
            try:
                user:User = UserUtils.dto_to_model(userDTO)
                session.add(user)
                # user = await UserService.add_to_db(user)
                userDTO = UserUtils.model_to_DTO(user=user)
                await session.commit()
                return userDTO.to_dict()
            except IntegrityError  as e:
                await session.rollback()
                return e
            except SQLAlchemyError as e:
                await session.rollback()
                return e
            finally:
                await session.close()
    
    
    async def read_one(self, id: int) -> dict | None | SQLAlchemyError:
        async with self.db.__crear_session() as session:
            try:
                user:User = session.get(self.Model, id)
                if user:
                    user_dto:UserDTO = UserUtils.model_to_DTO(user=user)
                    user_dto.to_dict()
                return user
            except IntegrityError | SQLAlchemyError  as e:
                db.session.rollback()
                return e
            finally:
                db.session.close()
            
    @staticmethod
    async def read_all() -> List[dict] | SQLAlchemyError:
        try:
            return [UserDTO(**user.to_dict()).to_dict() for user in await UserService.get_users()]
        except SQLAlchemyError | IntegrityError as e:
            db.session.rollback()
            return e
        finally:
            db.session.close()

    @staticmethod
    async def update(id: int, new_data: dict) -> dict:
        try:
            user = await UserService.get_user_by_id(id)
            if user:
                for key, value in new_data.items():
                    if key != "id":
                        setattr(user, key, value)
                db.session.commit()
                return UserDTO(**user.to_dict()).to_dict()
            else:
                raise ValueError("User not found")
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            db.session.close_all()

    @staticmethod
    async def delete(id: int) -> bool:
        try:  
            user = await UserService.get_user_by_id(id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return True
            return False
        except SQLAlchemyError | IntegrityError as e:
            db.session.rollback()
            return e
        finally:
            db.session.close()
    
    
    # async def get_user_by_id( id:int) -> User:
    #     return db.session.get(entity=User, ident=id)
        
    
    
    # async def get_users() -> List[User]:
    #     return db.session.query(User).all()
    
    # async def get_users_df(self):
    #     users = await UserService.read_all()
    #     return UserUtils.to_df(users)
    
    # async def add_to_db(user:User):
    #     try:
    #         db.session.add(user)
    #         db.session.commit()
            
    #         return user
    #     except SQLAlchemyError  as e:
    #         db.session.rollback()
    #         raise e
        
USER_SERVICE: UserService = UserService(db=db, Model=User)