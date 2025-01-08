from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели поста"""

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'create_at']

    def validate_content(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("Content is too long (max 500 characters).")
        return value
