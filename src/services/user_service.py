from typing import List
from sqlalchemy.exc import SQLAlchemyError, IntegrityError 
from config.db import db
from models.user_model import User
from dao.user_dao import UserDAO
from dto.user_dto import UserDTO
from utils.user_utils import UserUtils

class UserService(UserDAO):

    @staticmethod
    async def create(userDTO: UserDTO) -> dict | IntegrityError | SQLAlchemyError:
        try:
            user:User = UserUtils.dto_to_model(userDTO)
            user.password = user.set_password(userDTO.password)
            user = await UserService.add_to_db(user)
            userDTO = UserUtils.model_to_DTO(user=user)
            return userDTO.to_dict()
        except IntegrityError  as e:
            db.session.rollback()
            return e
        except SQLAlchemyError as e:
            db.session.rollback()
            return e
        finally:
            db.session.close()
    
    @staticmethod
    async def read_one(id: int) -> dict | None | SQLAlchemyError:
        try:
            user:User = await UserService.get_user_by_id(id)
            if user:
                user_dto:UserDTO = UserUtils.model_to_DTO(user=user)
                return user_dto.to_dict_list()
            return user
        except (IntegrityError , SQLAlchemyError)  as e:
            db.session.rollback()
            return e
        finally:
            db.session.close()
            
    @staticmethod
    async def read_all() -> List[dict] | SQLAlchemyError:
        try:
            return [UserDTO(**user.to_dict()).to_dict_list() for user in await UserService.get_users()]
        except (SQLAlchemyError , IntegrityError) as e:
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
        except (SQLAlchemyError , IntegrityError) as e:
            db.session.rollback()
            return e
        finally:
            db.session.close()
    
    
    async def get_user_by_id( id:int) -> User:
        return db.session.get(entity=User, ident=id)
        
    
    
    async def get_users() -> List[User]:
        return db.session.query(User).all()
    
    async def get_users_df():
        users = await UserService.read_all()
        return UserUtils.to_df(users)
    
    async def add_to_db(user:User):
        try:
            db.session.add(user)
            db.session.commit()
            
            return user
        except SQLAlchemyError  as e:
            db.session.rollback()
            raise e
        
    @staticmethod    
    async def get_user_by_username( username:str) -> User:
        try:
            user: User = db.session.query(User).filter_by(username=username).first()
            if user is not None:
                return user
            return None
        except Exception as e:
            print(f"Error: {e}")
user_service = UserService()