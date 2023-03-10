from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Book(models.Model):
    book_name = models.CharField('book_name', max_length=50)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_of_create = models.DateField('date_of_create')
    category = models.ManyToManyField(Category)

