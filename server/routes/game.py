from fastapi import APIRouter, status, Depends, HTTPException

from db import get_collections, list_games, serialize_game
from models import Game


router = APIRouter(
    tags=["games"],
)

@router.get("/games", status_code=status.HTTP_200_OK)
def get_games(collections: dict = Depends(get_collections)):
    data = collections["games"].find()
    games = list_games(data)
    return games

@router.post("/games", status_code=status.HTTP_201_CREATED)
def create_game(game: Game, collections: dict = Depends(get_collections)):
    new = collections["games"].insert_one(game.model_dump())
    inserted_game = collections["games"].find_one({"_id": new.inserted_id})
    return serialize_game(inserted_game)