from django.contrib import admin
from rango.models import Movie, Movie_review, UserProfile
from django.contrib import admin

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Movie)
admin.site.register(Movie_review)
