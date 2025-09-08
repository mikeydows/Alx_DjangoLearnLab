>>> from bookshelf.models import Book
>>> book =  Book.objects.get(title='1984')
>>> book
<Book: 1984 by author : George Orwell>
>>> book.title = '2000'
>>> book
<Book: 2000 by author : George Orwell>
>>> book.save()