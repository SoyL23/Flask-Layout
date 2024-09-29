from models.user_model import User
from dto.user_dto import UserDTO
from typing import List
from pandas import DataFrame
import pandas as pd

class UserUtils():

    def __init__(self) -> None:
        pass

    def model_to_DTO(user:User) -> UserDTO:
        print("Aqui")
        return UserDTO(**user.to_dict())

    def dto_to_model(userDTO:UserDTO) -> User:
        
        return User(**userDTO.to_dict())
    
    def to_df(users:List[UserDTO]) -> DataFrame:
        return pd.DataFrame([user.to_dict() for user in users])
        