from django.contrib import admin
from bookepedia.models import Book
from bookepedia.models import UserProfile
from bookepedia.models import Genre
from bookepedia.models import Comment

# Register your models here.

admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Genre)
admin.site.register(Comment)