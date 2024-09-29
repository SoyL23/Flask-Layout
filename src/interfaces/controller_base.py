from abc import ABC, abstractmethod

class Controller(ABC):

    @abstractmethod
    def create():
        pass

    @abstractmethod
    def get_one(id:int):
        pass

    @abstractmethod
    def get_all():
        pass

    @abstractmethod
    def edit(id:int, data:dict):
        pass

    @abstractmethod
    def remove(id:int):
        pass