from django.test import TestCase

from posts import services
from posts.models import Post
from posts.tests.factories import PostFactory
from users.tests.factories import UserFactory


class TestServices(TestCase):
    """
    Test case for posts services.
    """
    def test_post_create(self):
        self.assertEqual(0, Post.objects.count())
        post = services.post_create('text', UserFactory())
        self.assertEqual(1, Post.objects.count())
        self.assertEqual(post, Post.objects.first())

    def test_post_update(self):
        post = PostFactory()
        self.assertNotEqual('text', post.text)
        post = services.post_update(post, text='text')
        self.assertEqual('text', post.text)

    def test_post_delete(self):
        post = PostFactory()
        self.assertEqual(1, Post.objects.count())
        services.post_delete(post)
        self.assertEqual(0, Post.objects.count())
