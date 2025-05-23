from django.db import models
from movie.models import MovieModel


class CommentModels(models.Model):
    post = models.ForeignKey(
        MovieModel, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
