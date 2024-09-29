from abc import ABC, abstractmethod

class Route(ABC):

    @abstractmethod
    def post():
        pass

    @abstractmethod
    def get(id:int):
        pass

    @abstractmethod
    def get_list():
        pass

    @abstractmethod
    def put(id:int, data:dict):
        pass

    @abstractmethod
    def delete(id:int):
        pass