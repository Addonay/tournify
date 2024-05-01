from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from db import get_collections, list_managers, serialize_manager
from models import Manager


router = APIRouter(
    tags=["managers"],
)

@router.get("/managers",status_code=status.HTTP_200_OK)
def get_managers(collections: dict = Depends(get_collections)):
    data = collections["managers"].find()
    managers = list_managers(data)
    return managers

@router.post("/managers", status_code=status.HTTP_201_CREATED)
def add_manager(manager:Manager, collections: dict = Depends(get_collections)):
    new = collections["managers"].insert_one(manager.model_dump())
    inserted_manager = collections["managers"].find_one({"_id": new.inserted_id})
    return serialize_manager(inserted_manager)

@router.get("/managers/{manager_id}", status_code=status.HTTP_200_OK)
def get_manager(manager_id: str, collections: dict = Depends(get_collections)):
    manager = collections["managers"].find_one({"_id": ObjectId(manager_id)})
    if not manager:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Manager not found")
    else:
        return serialize_manager(manager)

