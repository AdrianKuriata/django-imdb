from django.db import models
from django.utils.text import Truncator
from django.utils.dateparse import parse_duration

class Movie(models.Model):
    genres = models.ManyToManyField('movies.genre', related_name='movies', blank=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    excerpt = models.CharField(max_length=120)
    cover = models.ImageField(upload_to='covers', null=True)
    description = models.TextField()
    release_date = models.DateField()
    duration_time = models.DurationField(null=True)

    def __str__(self):
        return self.title

    @property
    def converted_duration_time(self):
        return '{:02d}h {:02d}m'.format(*divmod(self.duration_time.seconds, 60))

    @property
    def truncated_excerpt(self):
        return Truncator(self.excerpt).chars(100)

class Genre(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)

    def __str__(self):
        return self.name
