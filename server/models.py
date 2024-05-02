from pydantic import BaseModel


class User(BaseModel):
    username: str
    
class Manager(BaseModel):
    username: str
    profile_pic:str
    
class Player(BaseModel):
    username: str
    profile_pic:str
    

class PlayerStats(BaseModel):
    goals: int
    assists: int

class Game(BaseModel):
    user: User
    players: list[Player]
    player_stats: dict[str, PlayerStats]
    total_goals: int