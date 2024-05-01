from pydantic import BaseModel


class User(BaseModel):
    username: str
    
class Manager(BaseModel):
    username: str
    profile_pic:str
    