from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)       # Book title
    author = models.CharField(max_length=100)      # Book author
    publication_year = models.IntegerField()       # Year of publication

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
