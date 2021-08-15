from django.db import models


# Create your models here.

class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g Science Fiction)")

    def __str__(self):
        """String for representing the Model object"""
        return self.name
