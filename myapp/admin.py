from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.BookSearch)
admin.site.register(models.MovieSearch)
