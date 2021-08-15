from django.db import models
from django.urls import reverse


# Create your models here.

class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g Science Fiction)")

    def __str__(self):
        """String for representing the Model object"""
        return self.name


class Book(models.Model):
    """Model representing a book (But not a specific copy of a book)"""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the Book")
    isbn = models.CharField('ISBN',
                            max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a> '
                            )

    genre = models.ManyToManyField(Genre, help_text="Select A genre for this book")

    def __str__(self):
        """String for Representing the model Object """
        return self.title

    def get_absolute_url(self):
        """Returning the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

