from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from routes import user

app = FastAPI()

app.include_router(user.router)
