from bson import json_util


class Notification:
    notification_type: str = "broadcast"
    event: str = "post_created"
    content: dict
    sender: str
    receiver: str
    topic: str = "default"
    token: str
    org: dict
    read: bool = False
    role: str

    def __init__(self, sender, content):
        self.sender = json_util.dumps(sender)
        self.content = content

    def data(self):
        data = {}
        data.update(vars(self))
        data.update({
            "notification_type": self.notification_type,
            "event": self.event,
            "content": self.content,
            "sender": self.sender
        })
        return data

    def message(self):
        message = {
            "data": self.data()
        }
        if self.is_broadcast():
            message['topic'] = self.topic
        else:
            message['token'] = self.token
        return message

    def is_broadcast(self):
        return bool(self.notification_type == "broadcast")
