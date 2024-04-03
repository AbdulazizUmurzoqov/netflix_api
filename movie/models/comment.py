from datetime import timezone

import data
from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie

# User = get_user_model()
# user_instance = User.objects.get(id=3)




class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    text = models.CharField(max_length=200)
    created_date = models.DateField()

# # comment = Comment.objects.create(user=user_instance)
# some_movie = Movie.objects.get(id=3)
# comment = Comment.objects.create(user=user_instance, movie_id=some_movie, text='Some text')
