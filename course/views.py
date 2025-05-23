from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import CourseModel
from .serializers import CourseSerializer
# Create your views here.


class CourseView(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ('course_created_at', 'course_rating')

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'ordering',
                openapi.IN_QUERY,
                description="Tartiblash",
                type=openapi.TYPE_STRING
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
