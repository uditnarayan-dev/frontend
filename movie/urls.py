
from django.urls import path, include
from movie import views

urlpatterns = [
    path('uploadmovie/', views.upload_movie, name="uploadmovie"),
    path('bookmovie/<int:id>/', views.bookmovie, name="bookmovie"),
    path('deletebooking/<int:id>/', views.delete_booking, name="deletebooking"),
    path('bookings/', views.my_bookings, name="my_bookings"),
]
