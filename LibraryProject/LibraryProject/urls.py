
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 
from bookshelf.views import SignUpView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("relationship_app.urls")),  # include app urls
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", TemplateView.as_view(template_name="accounts/profile.html"), name="profile"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
