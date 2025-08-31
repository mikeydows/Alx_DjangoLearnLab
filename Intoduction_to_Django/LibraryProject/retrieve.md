
**retrieve.md**
```markdown
```python
retrieved_book = Book.objects.get(id=book.id)
retrieved_book.title, retrieved_book.author, retrieved_book.publication_year
# ('1984', 'George Orwell', 1949)
