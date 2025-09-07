from .models import Library, Author, Book, Librarian

# 1. List all books in a library
def list_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    books = library.books.all()
    return books

# 2. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books

# 3. Retrieve the librarian for a library
def librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.librarian
