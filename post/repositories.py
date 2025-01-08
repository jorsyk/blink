from .models import Post, Like


class PostRepository:
    @staticmethod
    def get_by_id(post_id):
        return Post.objects.filter(id=post_id).first()

    @staticmethod
    def get_all():
        return Post.objects.all()


class LikeRepository:
    @staticmethod
    def get_or_create(user, post):
        return Like.objects.get_or_create(user=user, post=post)

    @staticmethod
    def delete(like):
        like.delete()
