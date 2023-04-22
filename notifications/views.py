from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.serializers import NotificationSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class SendNotification(APIView):
    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            notification = serializer.save()
            channel_layer = get_channel_layer()
            print(channel_layer)
            async_to_sync(channel_layer.group_send)(
                'notifications',
                {'type': 'notification', 'message': notification.message}
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
