from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

User = get_user_model()

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        target = get_object_or_404(User, id=user_id)
        request.user.following.add(target)
        target.followers.add(request.user)
        return Response({"detail": f"Now following {target.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "Cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        target = get_object_or_404(User, id=user_id)
        request.user.following.remove(target)
        target.followers.remove(request.user)
        return Response({"detail": f"Unfollowed {target.username}"}, status=status.HTTP_200_OK)
