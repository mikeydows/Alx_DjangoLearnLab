from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text='Comma-separated tags')

    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or len(content.strip()) < 2:
            raise forms.ValidationError("Comment must be at least 2 characters long.")
        return content
