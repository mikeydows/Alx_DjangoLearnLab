from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # existing field from step 1 (keep as-is)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    # NEW: explicit following field as required in this step
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_rel', blank=True)
