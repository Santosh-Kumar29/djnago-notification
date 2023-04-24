from django.utils import timezone


class Notification:
    def __init__(self, message, login_id):
        self.message = message
        self.login_id = login_id
        self.timestamp = timezone.now()
