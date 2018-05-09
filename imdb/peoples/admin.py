from django.contrib import admin
from .models import People, MoviePeople, PeopleType
# Register your models here.

admin.site.register(People)
admin.site.register(MoviePeople),
admin.site.register(PeopleType)
