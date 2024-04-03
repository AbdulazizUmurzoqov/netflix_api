from django.db import models
# from .movie import Movie

class Actor(models.Model):

    variants = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    birthdate = models.DateField(blank=True)
    gender = models.CharField(max_length=10, choices=variants, blank=True)


    class Meta:
        db_table = 'Actor'



    def __str__(self):
        return f'{self.last_name} {self.first_name}'