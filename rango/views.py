from http.client import HTTPResponse
from django.shortcuts import render
from django.urls import URLPattern, path
from rango.forms import MovieReviewsForm
from rango.forms import MovieForm
from rango import views
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

from rango.models import Movie

def index(request):

    index_movie_list = Movie.objects.order_by('movie_name')[:5]

    context_dict = {'movies': index_movie_list}

    return render(request, 'rango/index.html', context=context_dict)


def movies_list(request):
    context_dict = {}
    response = render(request, 'rango/movies_list.html', context=context_dict)
    return response


def user_personal_page(request):
    context_dict = {}
    response = render(request, 'rango/user_personal_page.html', context=context_dict)
    return response


def movie_detail_page(request):
    context_dict = {}

    response = render(request, 'rango/movie_detail_page.html', context=context_dict)
    return response


def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST) 
        if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                
                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']
                    profile.save()
                registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()
 
    return render(request,
    'rango/register.html',
    context = {'user_form': user_form,
     'profile_form': profile_form,
     'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('rango:index'))
            else:
                    return HttpResponse("you account is disable!!!!!")
        else:
            print("Invalid Login details:{username},{password}")
            return HttpResponse("Invalid Login detail supplied.")
    else:
        return render(request,'rango/login.html')        

def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index')) 


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES) 
        if  form.is_valid():
            profile = form.save(commit=False)
            if 'movie_image' in request.FILES:
                profile.movie_image = request.FILES['movie_image']
                profile.save()
                form.save()
        else:
            print(form.errors)
    else:
        form = MovieForm()
    return render(request,
    'rango/add_movie.html',
    context = {'form': form})

    
def add_movie_reviews(request):
    if request.method == 'POST':
        form = MovieReviewsForm(request.POST) 
        if  form.is_valid():
             form.save()
        else:
            print(form.errors)
    else:
        form = MovieReviewsForm()
    return render(request,
    'rango/add_movie_reviews.html',
    context = {'form': form})


