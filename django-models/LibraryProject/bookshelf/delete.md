>>> from bookshelf.models import Book    
>>> book = Book.objects.get(title=2000)  
>>> book                                
<Book: 2000 by author : George Orwell>
>>> book.delete()
(1, {'bookshelf.Book': 1})