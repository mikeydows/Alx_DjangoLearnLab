from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView,
)


urlpatterns = [
    path("", views.home, name = "home"),
    path("register/", views.register, name = "register"),
    path("login/", auth_views.LoginView.as_view(template_name = "blog/login.html"), name = "login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "blog/logout.html"), name="logout"),
    path('posts/', PostListView.as_view(), name = "post-list"),
    path('posts/new/', PostCreateView.as_view(), name = 'post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name = "post-detail"),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),
    path('search/', views.search_posts, name='search-posts'),
]