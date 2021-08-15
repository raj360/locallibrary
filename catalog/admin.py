from django.contrib import admin
from .models import BookInstance, Genre, Book, Author


class AuthorAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
# Register the admin class with the associated model
admin.site.register(Author,AuthorAdmin)
admin.site.register(BookInstance)
