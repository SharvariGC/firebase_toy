from fastapi import FastAPI
from bson.json_util import dumps
from app.server.firebase.notification_service.subscription_manager import subscribe, unsubscribe
from app.server.firebase.notification_service import notification_manager
from app.server.firebase.events.events import DummyEvent
from app.server.database.db import database
from app.server.services import user_service

app = FastAPI()


@app.get("/create_user")
async def read_root():
    user = {"email": "test@email.com"}
    database.users.insert_one(user)
    return dumps(user)

    
@app.post("/subscribe")
async def sub(device_token, user_id):
    subscribe(user_id, device_token)
    return {"message": "subscribed to topic!"}

@app.get("/unsubcribe")
async def unsub(user_id):
    unsubscribe(user_id)
    return {"message": "unsubscribed to topic!"}


@app.get("/test_notification")
async def test(sender, reciever):
    sender = user_service.get_user(sender)
    sender["_id"] = str(sender["_id"])
    notification_manager.send(DummyEvent(sender = sender, receiver = reciever))
    return {"message": "Firebase Test Notification"}