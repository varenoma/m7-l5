from rest_framework import serializers

from .models import MovieModel


class ListMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = '__all__'
