from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.text import slugify, Truncator

import re

class Movie(models.Model):
    genres = models.ManyToManyField('movies.genre', related_name='movies', blank=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, blank=True)
    excerpt = models.CharField(max_length=120)
    cover = models.ImageField(upload_to='covers', null=True)
    description = models.TextField()
    release_date = models.DateField()
    duration_time = models.DurationField(null=True)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        #Check saved movie has a PrimaryKey
        if self.pk is not None:
            #Get a Movie by PrimaryKey
            movie = get_object_or_404(Movie, pk=self.pk)

            #Check found movie has a equan saving slug
            if movie.slug == self.slug:
                return super(Movie, self).save(**kwargs)

        #Check if form sending slug, if yes, create slug from slug field, if no, create slug by title field
        if self.slug:
            slug = slugify(self.slug)
        else:
            slug = slugify(self.title)

        #Check if slug exists in database, if yes, create unique slug
        while Movie.objects.filter(slug=slug).exists():
            slug_suffix = re.search(r"(.*)-(\d$)", slug)

            if slug_suffix is not None:
                slug = '%s-%d' % (slug_suffix.group(1), int(slug_suffix.group(2)) + 1)
            else:
                slug = '%s-%d' % (slug, 1)

        #Save created slug
        self.slug = slug
        return super(Movie, self).save(**kwargs)

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
