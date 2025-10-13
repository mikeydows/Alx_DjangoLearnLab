from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author").prefetch_related("comments", "likes").all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content", "author__username"]
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        existing = Like.objects.filter(post=post, user=user)
        if existing.exists():
            return Response({"detail": "Already liked."}, status=status.HTTP_400_BAD_REQUEST)
        like = Like.objects.create(post=post, user=user)
        # create notification (deferred to notifications app via signal or direct import)
        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        existing = Like.objects.filter(post=post, user=user)
        if not existing.exists():
            return Response({"detail": "Not liked yet."}, status=status.HTTP_400_BAD_REQUEST)
        existing.delete()
        return Response({"detail": "Unliked."}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated], url_path="feed")
    def feed(self, request):
        # posts by users current user follows
        following = request.user.following.all()
        qs = Post.objects.filter(author__in=following).select_related("author").prefetch_related("comments", "likes").order_by("-created_at")
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        post_id = self.request.query_params.get("post")
        qs = Comment.objects.select_related("author", "post").all()
        if post_id:
            qs = qs.filter(post_id=post_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Create your views here.