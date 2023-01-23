from django.shortcuts import render,redirect
from .models import Rating,store_rating
from .forms import RatingForm
import datetime
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def rating_view(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        store_rating(rating)
        return redirect('success_page')
    return render(request, 'rating.html')

def store_rating(rating):
    if rating == "Good":
        good = 1
        average = 0
        bad = 0
    elif rating == "Average":
        good = 0
        average = 1
        bad = 0
    else:
        good = 0
        average = 0
        bad = 1
    rating = Rating(good=good, average=average, bad=bad, date=datetime.date.today())
    rating.save()

def success_page(request):
    return render(request, 'success.html')

def stats(request):
    ratings = Rating.objects.all()
    good_ratings = ratings.filter(good=True).count()
    average_ratings = ratings.filter(average=True).count()
    bad_ratings = ratings.filter(bad=True).count()

    context = {
        'good_ratings': good_ratings,
        'average_ratings': average_ratings,
        'bad_ratings': bad_ratings,
    }
    return render(request, 'stats.html', context)

def loginuser(request):
    if request.method=='GET':
        return render(request,'login.html',{'form':AuthenticationForm()})
    else:
        uname = request.POST['username']
        upwd = request.POST['password']
        user = authenticate(request, username=uname, password=upwd)
        if user is not None:
            login(request,user)
            return redirect('stats')
        else:
            return render(request,'login.html',{'form':AuthenticationForm(),'message':'User Not Found. Try Again'})

def logoutuser(request):
    logout(request)
    return redirect('rating')

