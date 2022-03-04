from django.shortcuts import render
from django.urls import URLPattern, path
from rango import views



# Create your views here.



def index(request):

    context_dict = {}

    response = render(request, 'rango/index.html', context=context_dict)
    return response


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
