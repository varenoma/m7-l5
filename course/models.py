from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class CourseModel(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    course_rating = models.FloatField(null=True, blank=True, validators=[
                                      MaxValueValidator(5), MinValueValidator(1)])
    course_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name
