from app.server.firebase.notification_service.notification import Notification
from bson import json_util


class DummyEvent(Notification):
    def __init__(self, sender, receiver):
        content = "Dummy"
        super(DummyEvent, self).__init__(sender, content)
        self.receiver = receiver
        self.notification_type = "single"
        self.event = "test event"
        self.sender = sender["_id"]
        self.token = sender["token"]
