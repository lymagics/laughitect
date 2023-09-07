from django.http import Http404
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
        with self.assertRaises(Http404):
            selectors.user_get(1)

    def test_user_list_selector(self):
        user = UserFactory()
        users = selectors.user_list()
        self.assertIn(user, users)
