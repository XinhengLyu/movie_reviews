from unicodedata import name
from django.urls import path
from rango import views

app_name = 'rango'


urlpatterns=[
    path('',views.index,name='index'),
    path('movies_list/',views.movies_list,name='movies_list'),
    path('user_personal_page/',views.user_personal_page,name='user_personal_page'),
    path('movie_detail_page/',views.movie_detail_page,name='movie_detail_page'),

]