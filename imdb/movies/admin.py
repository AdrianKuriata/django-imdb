from django.contrib import admin

from .models import Genre, Movie

from peoples.models import MoviePeople

class MoviePeopleInline(admin.TabularInline):
    model = MoviePeople

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (
            'title',
        )
    }

    inlines = [
        MoviePeopleInline,
    ]

admin.site.register(Genre)
