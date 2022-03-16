from django.db import models
from django.contrib.auth.models import User
from django import views
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    information = models.CharField(max_length=512)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

class Movie(models.Model):
    movie_name=models.CharField(max_length=128,unique=True)
    movie_information=models.CharField(max_length=1000,blank=False)
    release_date=models.DateField(blank=False)
    movie_image = models.ImageField(upload_to='Movie_images',blank=False)
    slug = models.SlugField(unique=True)
    trailer_link = models.URLField() 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.movie_name) 
        super(Movie, self).save(*args, **kwargs)     
   
    def __str__(self):
       return self.movie_name

class Movie_review(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews") 
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews") 
    review_content=models.CharField(max_length=2000,blank=False)
    likes_number=models.IntegerField(blank=False)
    dislikes_number=models.IntegerField(blank=False)
    create_time=models.DateField(auto_now_add=True)
    grade=models.IntegerField(blank=False)
    
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     grade=cleaned_data.get('grade')
    #     if grade>10 or grade<0:
    #         grade = f'0<grade<10'
    #         cleaned_data['grade'] = grade

    #     return grade
    def __str__(self):
       return self.review_content

#slug = models.SlugField(unique=True)