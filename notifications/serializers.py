from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
    timestamp = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Notification(**validated_data)
