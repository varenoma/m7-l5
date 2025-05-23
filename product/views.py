from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import ListProductSerializer
from .models import ProductModel
from .filters import ProductFilter


class ListProductView(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ListProductSerializer
    filter_backends = [DjangoFilterBackend]
    # http://127.0.0.1:8000/products/products/?min_price =15000&max_price=16000
    filterset_class = ProductFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'min_price',
                openapi.IN_QUERY,
                description="Minimal narx",
                type=openapi.TYPE_NUMBER
            ),
            openapi.Parameter(
                'max_price',
                openapi.IN_QUERY,
                description="Maksimal narx",
                type=openapi.TYPE_NUMBER
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
