from django.test import TestCase

from users import selectors
from users.tests.factories import UserFactory


class TestSelectors(TestCase):
    """
    Test case for user selectors.
    """
    def test_user_get_selector(self):
        new_user = UserFactory()
        user = selectors.user_get(new_user.pk)
        self.assertEqual(new_user, user)

    def test_user_get_selector_fail(self):
        user = selectors.user_get(1)
        self.assertIsNone(user)

    def test_user_list_selector(self):
        user = UserFactory()
        users = selectors.user_list()
        self.assertIn(user, users)

    def test_user_following_selector(self):
        user = UserFactory()
        other = UserFactory()
        user.follow(other)
        following = selectors.user_following(user)
        self.assertIn(other, following)

    def test_user_following_selector(self):
        user = UserFactory()
        other = UserFactory()
        user.follow(other)
        followers = selectors.user_followers(other)
        self.assertIn(user, followers)
