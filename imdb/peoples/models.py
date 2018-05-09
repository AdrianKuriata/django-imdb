from django.db import models

from movies.models import Movie

class People(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    born_date = models.DateField()
    born_place = models.CharField(max_length=120)

    def __str__(self):
        return self.first_name + ' ' + self.second_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.second_name

class MoviePeople(models.Model):
    people = models.ForeignKey('peoples.people', on_delete=models.CASCADE, related_name='movie_people')
    movie = models.ForeignKey('movies.movie', on_delete=models.CASCADE, related_name='movie_people')
    movie_name = models.CharField(max_length=120, blank=True)
    type = models.ForeignKey('peoples.peopletype', on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.movie.title + ' - ' + self.people.full_name + ' - ' + self.movie_name

class PeopleType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
