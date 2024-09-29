from abc import ABC, abstractmethod

class UserDAO(ABC):
    
    @abstractmethod
    def create(data:dict):
        pass

    @abstractmethod
    def read_one(id:int):
        pass

    @abstractmethod
    def read_all():
        pass
    
    @abstractmethod
    def update(id:int):
        pass

    @abstractmethod
    def delete(id:int):
        pass
    
    @abstractmethod
    def get_user_by_id(id:int):
        pass
    
    @abstractmethod
    def get_users():
        pass