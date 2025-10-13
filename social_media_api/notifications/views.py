from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from django.shortcuts import get_object_or_404

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by("-timestamp")

class NotificationMarkReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def patch(self, request, pk):
        notif = get_object_or_404(Notification, pk=pk, recipient=request.user)
        notif.unread = False
        notif.save()
        return Response(NotificationSerializer(notif).data, status=status.HTTP_200_OK)

