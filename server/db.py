from pymongo import MongoClient

def get_collections():
    client = MongoClient("mongodb+srv://addonayosoro:addo@newcluster.up0e1rl.mongodb.net/?retryWrites=true&w=majority&appName=newcluster")
    db = client.tournify
    collections = {
        "users": db.users,
        "managers": db.managers
    }
    return collections

def serialize_user(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"]
    }
    
def list_users(users) -> list:
    return [serialize_user(user) for user in users]

def serialize_manager(manager) -> dict:
    return {
        "id": str(manager["_id"]),
        "username": manager["username"],
        "profile_pic": manager["profile_pic"]
    }

def list_managers(managers) -> list:
    return [serialize_manager(manager) for manager in managers]