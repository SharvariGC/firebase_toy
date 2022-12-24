from app.server.firebase.notification_service import firebase



def send(notification):
    firebase.send(notification)

def send_dummy(notification):
    firebase.send(notification)
