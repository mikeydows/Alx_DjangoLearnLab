# CRUD Operations for Book Model

This document demonstrates the Create, Retrieve, Update, and Delete operations 
performed on the `Book` model using the Django shell.

---

## 1. Create

```python
from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Expected Output:
# <Book: 1984 by George Orwell (1949)>

## 2. Retrieve

```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()
# Expected Output:
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Retrieve a single book by title
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected Output:
# ('1984', 'George Orwell', 1949)


---

### 📘 3. Update
```markdown
## 3. Update

```python
from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

book
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>



---

### 📘 4. Delete
```markdown
## 4. Delete

```python
from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()

# Confirm deletion
Book.objects.all()
# Expected Output:
# <QuerySet []>
