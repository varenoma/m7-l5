from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import ArticleModel
from .serializers import ListArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = ArticleModel.objects.all()
    serializer_class = ListArticleSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author', 'category']
    search_fields = ['title', 'summary']
    ordering_fields = ['created_at']
    ordering = ['created_at']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('author', openapi.IN_QUERY,
                          description="Filter author", type=openapi.TYPE_INTEGER),
        openapi.Parameter('category', openapi.IN_QUERY,
                          description="Filter category", type=openapi.TYPE_INTEGER),
        openapi.Parameter('search', openapi.IN_QUERY,
                          description="Search summary", type=openapi.TYPE_STRING),
        openapi.Parameter('ordering', openapi.IN_QUERY,
                          description="Order created_at", type=openapi.TYPE_STRING),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
