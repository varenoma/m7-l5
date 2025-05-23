from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ListMovieView


router = DefaultRouter()

router.register('movies', ListMovieView, basename='movies')


urlpatterns = [
    path('', include(router.urls))
]
