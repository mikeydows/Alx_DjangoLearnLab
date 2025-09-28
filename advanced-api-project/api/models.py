from django.db import models


# We will define the Author and Book model
class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField("Publication Year")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



