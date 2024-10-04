from abc import ABC, abstractmethod
from dao.dao import DAO


class Controller(ABC):
    
    def __init__(self, service:DAO) -> None:
        self.__service:DAO = service
        super().__init__()

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get_one(self, id:int) -> dict:
        pass

    @abstractmethod
    def get_all(self) -> dict:
        pass

    @abstractmethod
    def edit(self, id:int, data:dict) -> dict:
        pass

    @abstractmethod
    def remove(self, id:int):
        pass