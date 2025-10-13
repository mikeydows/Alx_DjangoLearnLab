from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "author_username", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "author_username", "created_at", "updated_at"]

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "author", "author_username", "title", "content", "created_at", "updated_at", "comments", "likes_count"]
        read_only_fields = ["id", "author", "author_username", "created_at", "updated_at", "comments", "likes_count"]

    def get_likes_count(self, obj):
        return obj.likes.count()

class LikeSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Like
        fields = ["id", "post", "user", "user_username", "created_at"]
        read_only_fields = ["id", "user", "user_username", "created_at"]
