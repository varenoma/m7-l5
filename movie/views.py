from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import MovieModel
from .serializers import ListMovieSerializer
from .filters import MovieFilter


class ListMovieView(ModelViewSet):
    queryset = MovieModel.objects.all()
    serializer_class = ListMovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'title',
                openapi.IN_QUERY,
                description="title search",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'year',
                openapi.IN_QUERY,
                description="year search",
                type=openapi.TYPE_NUMBER
            ),
            openapi.Parameter(
                'genre',
                openapi.IN_QUERY,
                description="genre search",
                type=openapi.TYPE_STRING
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
