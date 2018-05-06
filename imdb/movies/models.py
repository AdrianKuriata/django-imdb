from django.db import models

class Movie(models.Model):
    genres = models.ManyToManyField('movies.genre', related_name='movies', blank=True)
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550, unique=True)
    excerpt = models.CharField(max_length=300)
    cover = models.ImageField(upload_to='covers', default=None)
    description = models.TextField()
    release_date = models.DateField()
    duration_time = models.DurationField()

    def __str__(self):
        return self.title

    @property
    def get_human_duration_time(self):
        return '{:02d}h {:02d}m'.format(*divmod(self.duration_time, 60))

    @property
    def get_cut_excerpt(self):
        cutted = self.excerpt[:100]
        return cutted + ' ...'

class Genre(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name
