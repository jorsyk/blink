from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели поста"""

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'created_at']
