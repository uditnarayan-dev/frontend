
from django.urls import path, include
from account import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    path('customer-home/', views.customer_home_view, name="customer_home"),
    path('seller-home/', views.seller_home_view, name="seller_home"),
]
