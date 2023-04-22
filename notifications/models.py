from django.utils import timezone


class Notification:
    def __init__(self, message):
        self.message = message
        self.timestamp = timezone.now()
