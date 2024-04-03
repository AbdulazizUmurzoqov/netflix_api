from django.db import models
from .actor import Actor

class Movie(models.Model):

    GENRES = (
        ('romantic', 'Romantic'),
        ('comedy', 'Comedy'),
        ('horror', 'Horror'),
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('thriller', 'Thriller')
    )

    name = models.CharField(max_length=150, blank=False, null=False)
    author = models.ForeignKey(Actor, on_delete=models.CASCADE, blank=True)
    year = models.DateField()
    genre = models.CharField(max_length=10, choices=GENRES)
    imdb = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Movie'

    def __str__(self):
        return f"{self.name} by {self.author}"