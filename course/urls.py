from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CourseView


router = DefaultRouter()

router.register('course', CourseView, basename='course')


urlpatterns = [
    path('', include(router.urls))
]
