from django.db import models
from django.urls import reverse
import uuid


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
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

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

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all())

    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('0', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        help_text="Book Availability",
        default='m',
        blank=True
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model Object"""
        return f'{self.id} ({self.book.id})'

    def display_id(self):
        """function to display a joint book id and instance id"""
        return f'{self.id} ({self.book.id})'


class Author(models.Model):
    """This model represents an Author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns a url to access a particular author url"""
        return reverse('author_detail', args=[str(self.id)])

    def __str__(self):
        """String representation of the Model Object"""
        return f"{self.last_name} {self.first_name}"
