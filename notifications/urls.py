from django.urls import path
from notifications.views import SendNotification
from notifications.consumer import clear_user_channel_layer

from notifications import consumer

from django.urls import path

urlpatterns = [
    path('send-notifications/<int:login_id>/', SendNotification.as_view()),
    path('clear-channel-layer/<str:login_id>/', clear_user_channel_layer, name='clear_user_channel_layer'),
]
