from rest_framework import serializers
from .models import Actor, Movie, Comment
from datetime import date
from rest_framework.exceptions import ValidationError

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'last_name', 'first_name', 'birthdate', 'gender')


    def validate_birthdate(self, value):
        if value < date(1950, 1, 1):
            raise ValidationError(detail='The time mus be high than 01.01.1950')
        return value

class MovieSerializer(serializers.ModelSerializer):

    author = ActorSerializer()

    class Meta:
        model = Movie
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')