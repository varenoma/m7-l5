from django.db import models

# Create your models here.


class MovieModel(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
