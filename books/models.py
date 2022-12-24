from django.db import models

class Book(models.Model):
    pages = models.IntegerField()
    title = models.CharField(max_length=255)
    author = models.ForeignKey('books.Author', on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=100)
    