from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(recipient, actor, verb, target=None):
    kwargs = {"recipient": recipient, "actor": actor, "verb": verb}
    if target is not None:
        kwargs["target_content_type"] = ContentType.objects.get_for_model(target.__class__)
        kwargs["target_object_id"] = target.id
    Notification.objects.create(**kwargs)
