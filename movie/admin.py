from django.contrib import admin
from movie.models import Movie, BookedMovies

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['seller', 'moviename', 'movieprice', 'movieimage']
    list_filter = ['seller', 'moviename']
    search_fields = ['seller__username', 'moviename']

@admin.register(BookedMovies)
class BookedMoviesAdmin(admin.ModelAdmin):
    list_display= ['customer', 'movie', 'booked_at']
    list_filter= ['customer', 'movie']
    search_fields= ['movie__moviename', 'customer__username']