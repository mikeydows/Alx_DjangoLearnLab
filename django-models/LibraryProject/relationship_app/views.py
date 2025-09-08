# from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book
from django import forms


# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'







# Registration view using built-in UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # use built-in form directly
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user immediately
            return redirect('list_books')  # redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})




# Admin view
@user_passes_test(lambda u: u.is_authenticated and u.profile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# Librarian view
@user_passes_test(lambda u: u.is_authenticated and u.profile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# Member view
@user_passes_test(lambda u: u.is_authenticated and u.profile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')




# Form for creating/updating books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

# Add Book view
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

# Edit Book view
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})

# Delete Book view
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})
