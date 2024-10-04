from abc import ABC, abstractmethod

class DAO(ABC):
    
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
    def update(id:int, data = dict):
        pass

    @abstractmethod
    def delete(id:int):
        pass
    