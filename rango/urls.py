from unicodedata import name
from django.urls import path
from rango import views

app_name = 'rango'
LOGIN_URL = 'rango:login'

urlpatterns=[
    path('',views.index,name='index'),
    path('movies_list/',views.movies_list,name='movies_list'),
    path('user_personal_page/',views.user_personal_page,name='user_personal_page'),
    path('movie_detail_page/<slug:movie_slug>/',views.movie_detail_page,name='movie_detail_page'),
    path('register/',views.register,name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('add_movie_reviews/<slug:movie_slug>/', views.add_movie_reviews, name='add_movie_reviews'),
    path('movie_suggestions/', views.movie_suggestions, name='movie_suggestions'),
    path('movie_search/', views.movie_search, name='movie_search'),
]