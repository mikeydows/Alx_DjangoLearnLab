from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm, PostForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q


def home(request):
    return render(request, "blog/home.html")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {'u_form': u_form, 'p_form': p_form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = "posts"
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post 
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    fields = ["title", "content"]
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()

        tags = form.cleaned_data['tags'].split(',')
        for tag_name in tags:
            tag_name = tag_name.strip()
            if tag_name:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    fields = ["title", "content"]
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()

        post.tags.clear()  # clear old tags before re-adding
        tags = form.cleaned_data['tags'].split(',')
        for tag_name in tags:
            tag_name = tag_name.strip()
            if tag_name:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

        return super().form_valid(form)

    
    def test_func(self):
        post = self.get.object()
        return self.request.user == post.author

    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get.object()
        return self.request.user == post.author

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})


def search_posts(request):
    query = request.GET.get('q')
    results = Post.objects.all()
    if query:
        results = results.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    return render(request, 'blog/search_results.html', {'query': query, 'results': results})


def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name__iexact=tag_name)
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag_name': tag_name})
