from django.contrib import admin
from rango.models import UserProfile,Movie,Movie_review
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('movie_name',)}

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Movie_review)