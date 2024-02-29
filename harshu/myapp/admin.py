from django.contrib import admin
from .models import Author,AuthorAdmin
admin.site.register(Author,AuthorAdmin)