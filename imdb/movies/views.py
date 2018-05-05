from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Movie

def index(request):
    movies = Movie.objects.all();

    return render(request, 'movies/index.html', {
            'movies': movies
    })

def show(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    return render(request, 'movies/show.html', {
        'movie': movie
    })
