from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Posts
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Search & Tags
    path('search/', views.search_posts, name='search_posts'),
    path('tags/<str:tag_name>/', views.tag_posts, name='tag_posts'),
]
