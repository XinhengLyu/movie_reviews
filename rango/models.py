from django.db import models
from django.contrib.auth.models import User
from django import views
from django.template.defaultfilters import slugify
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    information = models.CharField(max_length=512,blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

class Movie(models.Model):
    movie_name=models.CharField(max_length=128,unique=True)
    movie_information=models.CharField(max_length=1000,blank=False)
    release_date=models.DateField(blank=False)
    movie_image = models.ImageField(upload_to='Movie_images',blank=False)
    slug = models.SlugField(unique=True)
    trailer_link = models.URLField(default="/abc") 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.movie_name) 
        super(Movie, self).save(*args, **kwargs)     
   
    def __str__(self):
       return self.movie_name
    
    def get_average_rating(self):
        reviews = self.reviews.all()
        if reviews.count()>0:
            rating = round(reviews.aggregate(Avg("grade"))["grade__avg"],1)
            return rating
        else:
            return 0

class Movie_review(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE,related_name="reviews") 
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")      
    review_content=models.CharField(max_length=2000,blank=False)
    create_time=models.DateField(auto_now_add=True)
    grade=models.IntegerField(blank=False, default=1.0, validators=[MinValueValidator(1),MaxValueValidator(10)])  

    def __str__(self):
       return self.review_content