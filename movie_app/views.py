from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.


def show_all_movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/all_movies.html', {
        'movies_key': movies})


def show_one_movie(request, id_movie: int):
    # movie = Movie.objects.get(id=id_movie) - Если не найдёт введёный пользователем индекс,то будет ошибка DoesNotExist
    movie = get_object_or_404(Movie, id=id_movie)  # Если не найдёт введёный пользователем индекс,то будет ошибка pnf404
    return render(request, 'movie_app/one_movie.html', {'movie_key': movie})
