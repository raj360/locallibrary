from django.contrib import admin
from .models import BookInstance, Genre, Book, Author


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


class BookInstanceAdmin(admin.ModelAdmin):
    pass


# Register your models here.

admin.site.register(Genre)
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
