from django.urls import path
from notifications.views import SendNotification

from notifications import consumer

from django.urls import path


urlpatterns = [
    path('send-notifications/', SendNotification.as_view()),
]

