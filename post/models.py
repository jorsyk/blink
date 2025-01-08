from django.db import models

from user.models import User


class Post(models.Model):
    """
    Модель поста соцсети
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    """
    Модель лайков на посте в соцсети
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
