from .repositories import PostRepository, LikeRepository


def get_post_by_id(post_id):
    """
    Получить пост по его ID.
    """
    return PostRepository.get_by_id(post_id)


def toggle_like(user, post):
    """
    Логика добавления/удаления лайка.
    Возвращает сообщение о статусе действия.
    """
    like, create = LikeRepository.get_or_create(user, post)
    if not create:
        LikeRepository.delete(like)
        return 'Like removed'
    return 'Post liked'
