from rest_framework import serializers
from notifications.models import Notification

from rest_framework import serializers
from notifications.models import Notification
from django.utils import timezone


class NotificationSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
    # login_id = serializers.IntegerField()
    timestamp = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Notification(**validated_data)
