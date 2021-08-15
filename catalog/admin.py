from django.contrib import admin
from .models import BookInstance, Genre, Book, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(BookInstance)