from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Max, Min, Sum, Count, Avg

# Create your views here.


def show_all_movie(request):
    # movies = Movie.objects.all()  # Берём все объекты
    movies = Movie.objects.order_by('-rating', 'budget')
    # movies = Movie.objects.order_by(F('year').asc(null_last=True), '-rating') # Сортировка для null через F
    agg = movies.aggregate(Avg("budget"), Max("rating"), Min("rating"), Count("id"))
    return render(request, 'movie_app/all_movies.html', {
        'movies_key': movies,
        'agg_key': agg,
    })


def show_one_movie(request, slug_movie: str):
    # movie = Movie.objects.get(id=id_movie) - Если не найдёт введёный пользователем индекс (request, id_movie: int),то будет ошибка DoesNotExist
    movie = get_object_or_404(Movie, slug=slug_movie)  # Если не найдёт введёный пользователем slug,то будет ошибка pnf404
    return render(request, 'movie_app/one_movie.html', {'movie_key': movie})
