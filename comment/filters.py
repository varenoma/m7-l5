import django_filters
from .models import CommentModels


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = CommentModels
        fields = ['post']
