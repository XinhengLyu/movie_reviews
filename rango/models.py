from django.db import models
from django.contrib.auth.models import User
from django import views
from django.template.defaultfilters import slugify



class UserProfile(models.Model):
# This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
# The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

#movies
#id name information 


class Movie(models.Model):
    
    
    movie_name=models.CharField(max_length=128,unique=True)
    movie_information=models.CharField(max_length=512,blank=False)
    release_date=models.DateField(blank=False)
    movie_image = models.ImageField(upload_to='Movie_images', blank=False)

    def __str__(self):
       return self.movie_name


class Movie_review(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE) 
    user=models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    review_content=models.CharField(max_length=256,blank=False)
    likes_number=models.IntegerField(blank=False)
    dislikes_number=models.IntegerField(blank=False)
    creat_time=models.DateField(blank=False)

    def __str__(self):
       return self.user_id

slug = models.SlugField(unique=True)