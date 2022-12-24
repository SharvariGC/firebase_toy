from app.server.firebase.notification_service import firebase
from app.server.firebase.notification_service import subscription_manager
from app.server.services import user_service


def subscribe(user_id, token):
    firebase.subscribe(token)
    user_service.update_user(user_id, {"token": token})


def unsubscribe(user_id):
    user = user_service.get_user(user_id)
    firebase.unsubscribe(user['token']) if 'token' not in user else None
    user_service.update_user(user_id, {"token": None})

