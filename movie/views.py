from django.shortcuts import render, redirect
from movie.models import Movie, BookedMovies
from django.contrib import messages

def upload_movie(request):
    if request.method == "POST":
        seller = request.user
        moviename = request.POST.get('moviename')
        movieprice = request.POST.get('movieprice')
        movieimage = request.FILES.get('movieimage')

        movie= Movie.objects.create(
            seller= seller,
            moviename= moviename,
            movieprice= movieprice,
            movieimage= movieimage
        )
        messages.success(request, "Movie Created")
        return redirect('uploadmovie')
    
    return render(request, 'movie/movie_add.html')

def bookmovie(request, id):
    movie = Movie.objects.get(id = id)

    if BookedMovies.objects.filter(customer= request.user, movie= movie).exists():
        messages.info(request, "You already have booked this Movie")
        return redirect('my_bookings')
    
    book = BookedMovies.objects.create(
        customer= request.user,
        movie = movie
    )
    messages.success(request, "Movie booked successfully!")
    return redirect('my_bookings')

def my_bookings(request):
    bookings = BookedMovies.objects.filter(customer= request.user)
    return render(request, 'movie/booked.html', {'bookings':bookings})

def delete_booking(request, id):
    booking = BookedMovies.objects.get(id = id)
    if booking.customer != request.user:
        messages.info(request, "You are not allowed to delete this")
        return redirect('my_bookings')
    booking.delete()
    messages.info(request, "Booking Deleted Successfully")
    return redirect('my_bookings')

def nothing(request):
    pass