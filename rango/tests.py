from datetime import datetime
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rango.models import Movie, Movie_review, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import get_user

# Create your tests here.


class MovieTests(TestCase):
    def test_ensure_movie_page_loads(self):
        """ 
        Tests that movie detail page loads with the correct movie slug 
        """
        add_movie(name="Random Movie", info="random info")
        response = self.client.get(reverse("rango:movie_detail_page", 
                                    kwargs={'movie_slug':'random-movie'}))
        self.assertEqual(response.status_code, 200)

    def test_ensure_movie_page_contains_content(self):
        """
        Tests that movie detail page contains name, information and says No Reviews Yet
        """
        add_movie(name="Random Movie", info="random info")
        response = self.client.get(
            reverse("rango:movie_detail_page", kwargs={"movie_slug": "random-movie"}))
        self.assertContains(response, "Random Movie")
        self.assertContains(response, "random info")
        self.assertContains(response, "No reviews yet")


class UserTests(TestCase):
    def test_registration_login(self):
        """
        Tests that ensure users can register and login
        """
        username="testUser"
        password="Afairlylongpw%$123"
        create_test_user(client=self.client, username=username, password=password)
        login_test_user(client=self.client, username=username, password=password)
        self.assertTrue(get_user(self.client).is_authenticated)
    
    def test_user_personal_page(self):
        """
        Test for ensuring user personal page is active and contains username and info
        """
        username="testUser"
        password="Afairlylongpw%$123"
        create_test_user(client=self.client, username=username, password=password, info="abcxyz")
        login_test_user(client=self.client, username=username, password=password)
        response = self.client.get(reverse("rango:user_personal_page"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, username)
        self.assertContains(response, "abcxyz")

    def test_logout(self):
        """
        Tests that users can successfully logout after logging in
        """
        response_home_page = self.client.get(reverse("rango:index"))
        create_test_user(self.client)
        login_test_user(self.client)
        
        self.assertTrue(get_user(self.client).is_authenticated)

        self.client.get(reverse("rango:logout"))
        
        self.assertFalse(get_user(self.client).is_authenticated)

class MovieReviewTests(TestCase):
    def test_movie_reviews(self):
        """
        Test for ensuring that movie reviews can be posted
        """
        add_movie(name="Reviewed Movie")
        create_test_user(client=self.client)
        login_test_user(client=self.client)
        
        review_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
        self.client.post(reverse("rango:add_movie_reviews", kwargs={"movie_slug":"reviewed-movie"}),
                    {"review_content":review_content,"grade":5})
        response = self.client.get(reverse("rango:movie_detail_page", kwargs={"movie_slug":"reviewed-movie"}))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "testUser")
        self.assertContains(response, review_content)

class MovieListTests(TestCase):
    def test_movie_list_shows_movies(self):
        add_test_movies()
        response = self.client.get(reverse("rango:movies_list"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "First Movie")
        self.assertContains(response, "Second Movie")
        self.assertContains(response, "Third Movie")
        self.assertContains(response, "Fourth Movie")
        self.assertContains(response, "Fifth Movie")

class HomePageTests(TestCase):
    def test_homepage_shows_movies(self):
        add_test_movies()
        response = self.client.get(reverse("rango:index"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "First Movie")
        self.assertContains(response, "Second Movie")
        self.assertContains(response, "Third Movie")
        self.assertContains(response, "Fourth Movie")
        self.assertContains(response, "Fifth Movie")


def create_test_user(client, username="testUser", email="abc@xyz.com", password="Afairlylongpw%$123", info="random info", image="static/images/test_profile_picture.png"):
    """
    Creates a test user with the default username "testUser" and password "Afairlylongpw%$123"
    """
    client.post(reverse("rango:register"), {
        "username": username,
        "email": email,
        "password": password,
        "information": info,
        "picture": image
    })

def login_test_user(client, username="testUser", password="Afairlylongpw%$123"):
    """
    Logs in user witht the default test username and password 
    """
    client.post(reverse("rango:login"),
    {
        "username":username,
        "password":password
    })

def add_movie(name="Test Movie", info="abc123", release_date=datetime.now(), image="static/images/test_poster.jpeg", trailer_link="https://www.youtube.com/watch?v=DDjpOrlfh0Y"):
    movie = Movie(
        movie_name=name,
        movie_information=info,
        release_date=release_date,
        movie_image=image,
        trailer_link=trailer_link
    )
    movie.save()


def add_test_movies():
    add_movie(name="First Movie", info="random info for first movie")
    add_movie(name="Second Movie", info="random info for second movie")
    add_movie(name="Third Movie", info="random info for third movie")
    add_movie(name="Fourth Movie", info="random info for fourth movie")
    add_movie(name="Fifth Movie", info="random info for fifth movie")
