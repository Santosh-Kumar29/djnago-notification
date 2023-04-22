from django.urls import path
from notifications.consumer import NotificationConsumer
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

websocket_urlpatterns = [
    path('ws/connect-consumer/', NotificationConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
