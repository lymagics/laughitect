from django.test import TestCase

from posts import selectors
from posts.tests.factories import PostFactory


class TestSelectors(TestCase):
    """
    Test case for posts selectors.
    """
    def test_post_get(self):
        new_post = PostFactory()
        post = selectors.post_get(new_post.pk)
        self.assertEqual(post, new_post)

    def test_post_list(self):
        post = PostFactory()
        posts = selectors.post_list()
        self.assertEqual(1, len(posts))
        self.assertIn(post, posts)
