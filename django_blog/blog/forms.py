from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post, Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact = email).exists():
            raise forms.ValidationError("Email already exist")
        return email
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name"
        ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "bio",
            "image"
        ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content.strip()) == 0:
            raise forms.ValidationError("Comment cannot be empty.")
        return content