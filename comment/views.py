from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import CommentModels
from .serializers import CommentSerializer
from .filters import CommentFilter


class CommentViewSet(ModelViewSet):
    queryset = CommentModels.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter  # http://127.0.0.1:8000/comments/comments/?post=2
