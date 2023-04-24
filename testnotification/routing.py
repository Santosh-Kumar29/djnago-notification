from notifications.consumer import NotificationConsumer, clear_user_channel_layer
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

websocket_urlpatterns = [
    path('ws/connect-consumer/<str:login_id>/', NotificationConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
