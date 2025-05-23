from django.db import models

# Create your models here.


class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title