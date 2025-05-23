from rest_framework import serializers

from .models import ArticleModel


class ListArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = '__all__'