from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from db import get_collections, list_players, serialize_player
from models import Player


router = APIRouter(
    tags=["players"],
)

@router.get("/players",status_code=status.HTTP_200_OK)
def get_players(collections: dict = Depends(get_collections)):
    data = collections["players"].find()
    players = list_players(data)
    return players

@router.post("/players", status_code=status.HTTP_201_CREATED)
def add_player(player:Player, collections: dict = Depends(get_collections)):
    new = collections["players"].insert_one(player.model_dump())
    inserted_player = collections["players"].find_one({"_id": new.inserted_id})
    return serialize_player(inserted_player)

@router.get("/players/{player_id}", status_code=status.HTTP_200_OK)
def get_player(player_id: str, collections: dict = Depends(get_collections)):
    player = collections["players"].find_one({"_id": ObjectId(player_id)})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="player not found")
    else:
        return serialize_player(player)

