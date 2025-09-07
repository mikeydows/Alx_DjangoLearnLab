from django.urls import path
from . import views
from .views import register, CustomLoginView, CustomLogoutView, list_books, LibraryDetailView
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path("books/", list_books, name="book_list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    
    # Authentication
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),

    # Role-based views
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),

    # Book CRUD
    path("add-book/", views.add_book, name="add_book"),
    path("edit-book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete-book/<int:book_id>/", views.delete_book, name="delete_book"),
]
