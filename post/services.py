from django.shortcuts import get_object_or_404
from .models import Post, Like


def get_post_by_id(post_id):
    """Получить пост по его ID"""
    return get_object_or_404(Post, id=post_id)


def toggle_like(user, post):
    """
    Логика добавления/удаления лайка.
    Возвращает сообщение о статусе действия
    """
    like, created = Like.objects.get_or_create(user=user, post=post)
    if not created:
        like.delete()
        return 'Лайк удален'
    return 'Лайк поставлен'