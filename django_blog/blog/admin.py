from django.contrib import admin
from .models import Profile, Post
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)

admin.site.register(Post)
