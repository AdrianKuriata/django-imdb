from django.contrib import admin

from .models import Genre, Movie
from django.utils.text import slugify

import re

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (
            'title',
        )
    }

admin.site.register(Genre)
