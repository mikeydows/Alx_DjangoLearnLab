from relationship_app.models import Author, Book, Library, Librarian


def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)

        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")


def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # ManyToMany relationship

        print(f"Books in library '{library.name}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")


def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # OneToOne relationship

        print(f"Librarian for library '{library.name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library: {library_name}")


# Example usage when running in Django shell
if __name__ == "__main__":
    get_books_by_author("John Doe")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")


#Librarian.objects.get(library=