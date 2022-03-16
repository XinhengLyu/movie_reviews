from django import forms
from django.contrib.auth.models import User
from rango.models import Movie_review
from rango.models import Movie
from rango.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('information','picture',)


class MovieForm(forms.ModelForm):

    movie_name=forms.CharField(max_length=128, help_text="Please enter the movie name.",required=False) 
    movie_information=forms.CharField(max_length=128, help_text="Please enter the movie informatio.",required=False) 
    release_date= forms.DateField(label='time', widget=forms.SelectDateWidget,required=False)
    movie_image=forms.ImageField()
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = Movie
        fields = ('movie_name','movie_information','release_date','movie_image')
class MovieReviewsForm(forms.ModelForm):

    # movie=forms.IntegerField()
    # user=forms.IntegerField()
    # review_content=forms.CharField(max_length=256)
    # likes_number=forms.IntegerField()
    # dislikes_number=forms.IntegerField()
    # # creat_time=forms.DateField()
    # grade=forms.IntegerField()
    class Meta:
        model = Movie_review
        fields = ('review_content','grade')



