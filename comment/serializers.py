from rest_framework import serializers
from .models import CommentModels


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModels
        fields = '__all__'
