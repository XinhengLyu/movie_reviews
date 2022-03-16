from django.contrib import admin
from rango.models import UserProfile,Movie,Movie_review
from django.contrib import admin

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Movie)
admin.site.register(Movie_review)