from fastapi import APIRouter, Depends, HTTPException, status
from db import get_collections,list_users
from models import User

router = APIRouter(
    tags=["users"],
)

@router.get("/users")
def get_users(collections: dict = Depends(get_collections)):
    data = collections["users"].find()
    users = list_users(data)
    return users

@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User, collections: dict = Depends(get_collections)):
    collections["users"].insert_one(user.model_dump())
    return {"message": "User created"}
    
