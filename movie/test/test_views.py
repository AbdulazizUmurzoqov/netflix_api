# from django.test import TestCase
# from rest_framework.test import APIClient
# from django.urls import reverse
# from rest_framework import status
# from datetime import date
#
# from movie.models import Movie, Actor
#
#
# # class MovieViewSetTestCase(TestCase):
# #     def setUp(self):
# #         client = APIClient()
# #
# #         author = Actor.objects.create(first_name='Test', last_name='Author',birthdate=date(1990, 1, 1)
# # )
# #         Movie.objects.create(
# #             author='Test author',
# #             name=author,
# #             year='2001-03-02',
# #             genre='Drama'
# #         )
# #
# #         Movie.objects.create(
# #             author='Test author2',
# #             name=author,
# #             year='2001-04-02',
# #             genre='Thriller'
# #         )
#
# class MovieModelTestCase(TestCase):
#     def setUp(self):
#         # Create an instance of Actor
#         author = Actor.objects.create(
#             first_name='Test',
#             last_name='Author',
#             # birthdate=date(1990, 1, 1)  # Provide a birthdate value
#         )
#
#         # Assign the author to the movie
#         Movie.objects.create(
#             name='Test movie1',
#             author=author,
#             year='2001-03-02',
#             genre='Drama'
#         )
#
#         Movie.objects.create(
#             name='Test movie2',
#             author=author,
#             year='2001-04-02',
#             genre='Thriller'
#         )
#
#     def test_movie_list(self):
#         url = reverse('movie-list')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, status.HTTP_200_OK)
#         self.assertEquals(len(response.data), 2)

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from movie.models import Movie

class MovieViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Movie.objects.create(title='Test Movie 1', imdb=8.5)
        Movie.objects.create(title='Test Movie 2', imdb=7.9)
        Movie.objects.create(title='Test Movie 3', imdb=6.3)

    def test_list_movies(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Ensure all movies are listed

    def test_search_movies(self):
        url = reverse('movie-list') + '?search=Test Movie 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure only one movie is found

    def test_order_movies_by_imdb(self):
        url = reverse('movie-list') + '?ordering=imdb'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Ensure movies are listed in ascending order of IMDb ratings
        self.assertEqual(response.data[0]['title'], 'Test Movie 3')
        self.assertEqual(response.data[1]['title'], 'Test Movie 2')
        self.assertEqual(response.data[2]['title'], 'Test Movie 1')