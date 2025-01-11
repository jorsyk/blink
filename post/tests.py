from django.test import TestCase
from user.models import User
from post.models import Post, Like
from post.services import toggle_like

from post.repositories import PostRepository, LikeRepository


class ToggleLikeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(author=self.user, content='Test content')

    def test_toggle_like_creates_like(self):
        message = toggle_like(self.user, self.post)
        self.assertEqual(message, 'Post liked')
        self.assertTrue(Like.objects.filter(user=self.user, post=self.post).exists())

    def test_toggle_like_removes_like(self):
        Like.objects.create(user=self.user, post=self.post)
        message = toggle_like(self.user, self.post)
        self.assertEqual(message, 'Like removed')
        self.assertFalse(Like.objects.filter(user=self.user, post=self.post).exists())


class PostRepositoryTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post1 = Post.objects.create(author=self.user, content='first post')
        self.post2 = Post.objects.create(author=self.user, content='second post')

    def test_get_by_id(self):
        post_by_id = Post.objects.filter(id=self.post1.id).first()
        self.assertEqual(post_by_id, self.post1)

        self.assertTrue(Post.objects.filter(id=self.post1.id).exists())

    def test_get_by_id_nonexistent(self):
        post_by_id = Post.objects.filter(id=9999).first()
        self.assertIsNone(post_by_id)

    def test_get_all(self):
        posts = PostRepository.get_all()
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0], self.post1)
        self.assertEqual(posts[1], self.post2)


from django.test import TestCase
from user.models import User
from post.models import Post, Like
from post.repositories import LikeRepository


class LikeRepositoryTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(author=self.user, content='Test post')

    def test_get_or_create_creates_like(self):
        like, created = LikeRepository.get_or_create(self.user, self.post)
        self.assertTrue(created)
        self.assertEqual(like.user, self.user)
        self.assertEqual(like.post, self.post)

    def test_get_or_create_retrieves_existing_like(self):
        existing_like = Like.objects.create(user=self.user, post=self.post)
        like, created = LikeRepository.get_or_create(self.user, self.post)
        self.assertFalse(created)
        self.assertEqual(like, existing_like)

    def test_delete_like(self):
        like = Like.objects.create(user=self.user, post=self.post)
        LikeRepository.delete(like)
        self.assertFalse(Like.objects.filter(id=like.id).exists())
