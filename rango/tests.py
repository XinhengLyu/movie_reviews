from datetime import datetime
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
import tempfile 
from rango.models import Movie, Movie_review
# Create your tests here.

class MovieTests(TestCase):
    def test_ensure_movie_page_loads(self):
        """ 
        Tests that movie detail page loads with the correct movie slug 
        """
        add_movie(name="Random Movie", info="random info")
        response = self.client.get(reverse("rango:movie_detail_page", kwargs={'movie_slug':"random-movie"}))
        self.assertEqual(response.status_code, 200)
        
    def test_ensure_movie_page_contains_content(self):
        """
        Tests that movie detail page contains name, information and says No Reviews Yet
        """
        add_movie(name="Random Movie", info="random info")
        response = self.client.get(reverse("rango:movie_detail_page", kwargs={"movie_slug":"random-movie"}))
        self.assertContains(response, "Random Movie") 
        self.assertContains(response, "random info")
        self.assertContains(response, "No reviews yet")

class MovieReviewTests(TestCase):
    def test_movie_reviews(self):
        print("nothing")



def add_movie(name, info, release_date=datetime.now(), image="static/images/test_poster.jpeg", trailer_link="https://www.youtube.com/watch?v=DDjpOrlfh0Y"):
    movie = Movie(
        movie_name=name,
        movie_information=info,
        release_date=release_date,
        movie_image= image,
        trailer_link = trailer_link
        )
    movie.save()

def add_test_movies():
    add_movie("First Movie", "random info for first movie")
    add_movie("Second Movie", "random info for second movie")
    add_movie("Third Movie","random info for third movie")
    add_movie("Fourth Movie", "random info for fourth movie")
    add_movie("Fifth Movie", "random info for fifth movie")
     