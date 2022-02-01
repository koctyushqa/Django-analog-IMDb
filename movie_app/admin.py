from django.contrib import admin
from .models import Movie


# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status']
    list_editable = ['rating', 'year', 'budget']
    ordering = ['-rating', '-name']
    list_per_page = 10

    @admin.display(ordering='rating', description='Оценка зрителей')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Зря потратишь время!'
        if mov.rating < 70:
            return 'Разок можно глянуть.'
        if mov.rating <= 85:
            return 'Приятного просмотра.'
        if mov.rating <= 100:
            return 'Шедевр!'
