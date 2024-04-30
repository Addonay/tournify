from pymongo import MongoClient

def get_collections():
    client = MongoClient("mongodb+srv://addonayosoro:addo@newcluster.mongodb.net/?retryWrites=true&w=majority")
    db = client.tournify
    collections = {
        "users": db["users"]
    }
    return collections

def serialize_user(user) -> dict:
    return {
        "id": user["_id"],
        "username": user["username"]
    }
    
def list_users(users) -> list:
    return [serialize_user(user) for user in users]