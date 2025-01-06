from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя"""

    class Meta:
        model = User
        fields = ['id', 'username', 'description', 'profile_picture']
