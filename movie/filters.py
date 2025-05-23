import django_filters
from .models import MovieModel


class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = MovieModel
        fields = {
            'title': ['icontains'],
            'year': ['exact'],
            'genre': ['exact'],
        }