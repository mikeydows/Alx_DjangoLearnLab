>>> from bookshelf.models import Book
>>> books = Book.objects.all()
>>> books
<QuerySet [<Book: 1984 by author : George Orwell>]>
>>> books[0]
<Book: 1984 by author : George Orwell>
>>>