from channels.generic.websocket import AsyncWebsocketConsumer
from notifications.models import Notification
import json


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'notifications',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'notifications',
            self.channel_name
        )

    async def notification(self, event):
        message = event['message']
        notification = Notification(message)
        await self.send(text_data=json.dumps({
            'message': notification.message,
            'timestamp': str(notification.timestamp),
        }))
