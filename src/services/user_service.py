from sqlalchemy.exc import SQLAlchemyError, IntegrityError 
from dao.user_dao import UserDAO
from config.db import db
from models.user_model import User
from typing import List
from dto.user_dto import UserDTO
from utils.user_utils import UserUtils

class UserService(UserDAO):

    @staticmethod
    def create(userDTO: UserDTO) -> dict | IntegrityError | SQLAlchemyError:
        try:
            
            user:User = UserUtils.dto_to_model(userDTO)
            db.session.add(user)
            db.session.commit()
            user_dto:UserDTO = UserUtils.model_to_DTO(user=user)
            return user_dto.to_dict()
        except IntegrityError as e:
            db.session.rollback()
            return e
        except SQLAlchemyError as e:
            db.session.rollback()
            return e
        finally:
            db.session.close()
    
    @staticmethod
    def read_one(id: int) -> dict | None | SQLAlchemyError:
        try:
            user:User = UserService.get_user_by_id(id)
            if user:
                user_dto:UserDTO = UserUtils.model_to_DTO(user=user)
                return user_dto.to_dict()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            return e
        finally:
            db.session.close()
            
    @staticmethod
    def read_all() -> List[dict] | SQLAlchemyError:
        try:
            return [UserDTO(**user.to_dict()).to_dict() for user in UserService.get_users()]
        except SQLAlchemyError as e:
            db.session.rollback()
            return e
        finally:
            db.session.close()
        
        
  
    @staticmethod
    def update(id: int, new_data: dict) -> dict:
        try:
            user = UserService.get_user_by_id(id)
            if user:
                for key, value in new_data.items():
                    if key != "id":
                        setattr(user, key, value)
                db.session.commit()
                return UserDTO(**user.to_dict()).to_dict()
            else:
                raise ValueError("User not found")
        except IntegrityError as e:
            db.session.rollback()
            raise e
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close_all()

    @staticmethod
    def delete(id: int) -> bool:
        try:  
            user = UserService.get_user_by_id(id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            db.session.rollback()
            return e
        finally:
            db.session.close()
    
    @staticmethod
    def get_user_by_id(id:int) -> User:
        return db.session.get(entity=User, ident=id)
        
    
    @staticmethod
    def get_users() -> List[User]:
        return db.session.query(User).all()
        
user_service = UserService()