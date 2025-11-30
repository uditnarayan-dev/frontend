from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from account.models import UserProfile
from movie.models import Movie

def home_view(request):
    user = request.user
    if user.is_authenticated:
        if user.userprofile.role == 'seller':
            return redirect('seller_home')
        else:
            return redirect('customer_home')
        
    return render(request, 'account/home.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        nickname = request.POST.get('nickname')
        role = request.POST.get('role')

        if password1 != password2:
            messages.error(request, "Confirm Password didn't match")
            return redirect('register')
        
        if User.objects.filter(username= username).exists():
            messages.info(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username= username)
        user.set_password(password1)
        user.save()

        profile = UserProfile.objects.create(user= user, role= role, nick_name= nickname)
        
        messages.success(request, "User Created successfully")
        return redirect('login')

    return render(request, 'account/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username= username, password= password)
        if user:
            login(request, user)
            if user.userprofile.role == 'seller':
                return redirect('seller_home')
            else:
                return redirect('customer_home')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, 'account/login.html')

def customer_home_view(request):
    movies = Movie.objects.all()
    return render(request, 'account/customer_home.html', {'movies':movies})

def seller_home_view(request):
    movies = Movie.objects.all()
    return render(request, 'account/seller_home.html', {'movies':movies})

def logout_view(request):
    logout(request)
    return redirect('home')
