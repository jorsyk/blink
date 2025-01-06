from post.models import Post


def get_feed_post():
    """Возвращает все посты, отсортированные по дате создания"""
    return Post.objects.all().order_by('-created_at')
