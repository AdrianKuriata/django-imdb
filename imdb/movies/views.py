from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Movie

def index(request):
    movies_list = Movie.objects.all();
    counter_movies = movies_list.count

    paginator = Paginator(movies_list, 12)
    page = request.GET.get('page')
    movies = paginator.get_page(page)

    return render(request, 'movies/index.html', {
            'movies': movies,
            'counter_movies': counter_movies
    })

def show(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    return render(request, 'movies/show.html', {
        'movie': movie
    })

def genre(request, slug):
    genres_list = Movie.objects.filter(genres__slug=slug)
    counter_movies = genres_list.count

    paginator = Paginator(genres_list, 12)
    page = request.GET.get('page')
    genres = paginator.get_page(page)

    return render(request, 'movies/genre.html', {
        'genres': genres,
        'counter_movies': counter_movies
    })
