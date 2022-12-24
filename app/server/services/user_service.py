from app.server.database.db import database
from bson import ObjectId

def update_user(user_id, data):
    database.users.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": data})
    return "done!"

def get_user(user_id):
    return database.users.find_one({"_id": ObjectId(user_id)})