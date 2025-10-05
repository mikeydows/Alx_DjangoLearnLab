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
    tags = forms.CharField(
        required=False,
        help_text="Add comma-separated tags (e.g., django, python, web)"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Handle tags manually
        tag_names = [t.strip() for t in self.cleaned_data['tags'].split(',') if t.strip()]
        tags = []
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        instance.tags.set(tags)
        return instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body.strip()) < 5:
            raise forms.ValidationError("Comment is too short.")
        return body

