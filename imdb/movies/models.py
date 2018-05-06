from django.db import models
from django.utils.text import Truncator


class Movie(models.Model):
    genres = models.ManyToManyField('movies.genre', related_name='movies', blank=True)
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550, unique=True)
    excerpt = models.CharField(max_length=300)
    cover = models.ImageField(upload_to='covers', default=None)
    description = models.TextField()
    release_date = models.DateField()
    duration_time = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

    @property
    def get_human_duration_time(self):
        return '{:02d}h {:02d}m'.format(*divmod(self.duration_time, 60))

    @property
    def truncated_excerpt(self):
        return Truncator(self.excerpt).chars(100)

class Genre(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name
