from pymongo import MongoClient

def get_collections():
    client = MongoClient("mongodb+srv://addonayosoro:addo@newcluster.up0e1rl.mongodb.net/?retryWrites=true&w=majority&appName=newcluster")
    db = client.tournify
    collections = {
        "users": db.users,
        "managers": db.managers,
        "players": db.players,
        "player_stats": db.player_stats,
        "games": db.games
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

def serialize_player(player) -> dict:
    return {
        "id": str(player["_id"]),
        "username": player["username"],
        "profile_pic": player["profile_pic"]
    }

def list_players(players) -> list:
    return [serialize_manager(player) for player in players]

def serialize_game(game) -> dict:
    return {
        "id": str(game["_id"]),
        "user": game["user"],
        "players": game["players"],
        "player_stats": game["player_stats"],
        "total_goals": game["total_goals"]
    }
    
def list_games(games) -> list:
    return [serialize_game(game) for game in games]