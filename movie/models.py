from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Movie(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    moviename = models.CharField(max_length=200)
    movieprice = models.DecimalField(max_digits=10, decimal_places=2)
    movieimage = models.ImageField(upload_to="movies/")

    
class BookedMovies(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(default=timezone.now)