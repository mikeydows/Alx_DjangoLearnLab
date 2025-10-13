from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source="actor.username", read_only=True)
    class Meta:
        model = Notification
        fields = ["id", "recipient", "actor", "actor_username", "verb", "unread", "timestamp"]
        read_only_fields = ["id", "recipient", "actor_username", "timestamp"]
