from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),          # List all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View single post
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),       # Create new post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Edit post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='add_comment'),
    path('comments/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='delete_comment'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Search & Tags
    path('search/', views.search_posts, name='search_posts'),
    path('tags/<str:tag_name>/', views.tag_posts, name='tag_posts'),
]

