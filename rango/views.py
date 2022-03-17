from http.client import HTTPResponse
from django.forms import model_to_dict
from django.shortcuts import render
from django.urls import URLPattern, path
from rango.models import Movie,UserProfile
from rango.forms import MovieReviewsForm
from rango.forms import MovieForm
from rango import views
from rango.forms import UserForm, UserProfileForm,Movie_review
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Avg

# Create your views here.


def index(request):
    context_dict={}
    context_dict['movies'] = Movie.objects.all()
    return render(request, 'rango/index.html', context=context_dict)


def movies_list(request):
    context_dict={}
    context_dict['movies'] = Movie.objects.all()
    response = render(request, 'rango/movies_list.html', context=context_dict)
    return response


def user_personal_page(request):
    id = request.user.id
    obj = UserProfile.objects.get(user_id=id)
    objdic = model_to_dict(obj)

    comment = []
    commentList = Movie_review.objects.filter(user_id=id).values()
    for item in commentList:
        commentObj = {}
        commentObj["comment"] = item["review_content"]
        commentObj["grade"] = item["grade"]
        commentObj["likes_number"] = item["likes_number"]
        commentObj["dislikes_number"] = item["dislikes_number"]
        commentObj["create_time"] = item["create_time"]
        movieObJ = model_to_dict(Movie.objects.get(id=item["movie_id"]))
        commentObj["movie_name"] = movieObJ["movie_name"]
        commentObj["movie_image"] = movieObJ["movie_image"]
        commentObj["release_year"]=movieObJ["release_date"].strftime("%Y")
      
        comment.append(commentObj)
    context_dict = {"objdic": objdic,"comment":comment}
    response = render(request, 'rango/user_personal_page.html', context=context_dict)
    return response


def movie_detail_page(request, movie_slug):
    context_dict = {}
    movie = Movie.objects.get(slug = movie_slug)
    context_dict['movie'] = movie
    context_dict['form'] = MovieReviewsForm()
    reviews = movie.reviews.all()
    context_dict['reviews'] = reviews
    trailer = movie.trailer_link.split("v=")[1].split("&")[0]
    context_dict['trailer'] = trailer

    if reviews:
        context_dict['average_rating'] = movie.get_average_rating()
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



def add_movie_reviews(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)

    if not request.user.is_authenticated:
        return HttpResponse("Must be logged in to submit a review")

    previous_review_by_user = movie.reviews.filter(user=request.user)
    if previous_review_by_user:
        return HttpResponse("Cannot submit review for the same movie twice")

    if request.user.is_superuser:
        return HttpResponse("Admins cannot submit reviews. Please log in as a regular user")


    if request.method == 'POST':
        form = MovieReviewsForm(request.POST) 
        if  form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.likes_number = 0
            review.dislikes_number = 0
            review.user = request.user
            review.save()
            form = MovieReviewsForm()
        else:
            print(form.errors)
    else:
        form = MovieReviewsForm()
    context_dict = {}
    context_dict['movie'] = movie
    reviews = movie.reviews.all()
    context_dict['average_rating'] = round(reviews.aggregate(Avg("grade"))["grade__avg"],1)
    context_dict['form'] = form
    context_dict['reviews'] = reviews
    return render(request,'rango/movie_detail_page.html',context=context_dict)