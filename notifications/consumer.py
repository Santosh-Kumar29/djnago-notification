from channels.generic.websocket import AsyncWebsocketConsumer
from notifications.models import Notification
import json
from channels.layers import get_channel_layer
from django.http import HttpResponse


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        login_id = self.scope['url_route']['kwargs']['login_id']
        await self.channel_layer.group_add(f'notifications_{login_id}', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        login_id = self.scope['url_route']['kwargs']['login_id']
        await self.channel_layer.group_discard(f'notifications_{login_id}', self.channel_name)

    async def notification(self, event):
        message = event['message']
        login_id = event['login_id']
        notification = Notification(message, login_id)
        await self.send(
            text_data=json.dumps({'message': notification.message, 'timestamp': str(notification.timestamp)}))


# for clear memory logs
def clear_user_channel_layer(request, login_id):
    group_name = f'notifications_{login_id}'

    channel_layer = get_channel_layer()

    channel_layer.group_discard(group_name, None)

    return HttpResponse(f'Memory cleared for user {login_id}.')
