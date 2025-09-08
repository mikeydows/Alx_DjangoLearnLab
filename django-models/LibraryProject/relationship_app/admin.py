from django.contrib import admin
from .models import Author, Librarian, Library, Book

#  Register your models here.

admin.site.register([Book, Librarian, Library, Author])
