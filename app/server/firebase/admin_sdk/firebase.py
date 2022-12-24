from firebase_admin import messaging
import firebase_admin
from firebase_admin import credentials


default_app = firebase_admin.initialize_app()


cred = credentials.Certificate("config.json")
firebase_admin.initialize_app(cred)


def send(notification: Notification):
    message = messaging.Message(**notification.message())
    try:
        response = messaging.send(message)
        return response
    except Exception:
        pass


def subscribe(token: str, topic: str = "default"):
    response = messaging.subscribe_to_topic([token], topic)
    return response.success_count


def unsubscribe(token: str, topic: str = "default"):
    response = messaging.unsubscribe_from_topic([token], topic)
    return response.success_count
