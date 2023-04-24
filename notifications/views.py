from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.serializers import NotificationSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class SendNotification(APIView):
    def post(self, request, login_id):
        if not login_id:
            return Response("Provide login id", status=400)
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            notification = serializer.save(login_id=login_id)
            channel_layer = get_channel_layer()
            print(channel_layer)
            async_to_sync(channel_layer.group_send)(
                f'notifications_{login_id}',
                {'type': 'notification', 'message': notification.message, 'login_id': login_id}
            )
            response_data = serializer.data
            response_data['login_id'] = login_id
            return Response(response_data, status=200)
        return Response(serializer.errors, status=400)
