from django.core.exceptions import ValidationError
from django.test import TestCase

from users import services
from users.models import User
from users.tests.factories import UserFactory


class TestServices(TestCase):
    """
    Test case for user services.
    """
    def test_user_create_service(self):
        self.assertEqual(0, User.objects.count())
        user = services.user_create(
            'bob@example.com', 'bob', 'testpass123',
        )
        self.assertEqual(1, User.objects.count())
        self.assertEqual(user, User.objects.first())

    def test_user_create_service_fail_if_username_in_user(self):
        user = UserFactory()
        with self.assertRaises(ValidationError):
            services.user_create(
                user.email, user.username, user.password,
            )

    def test_user_update_service(self):
        user = UserFactory()
        updated = services.user_update(
            user.id, username='bob', password='catdog',
        )
        user.refresh_from_db()
        self.assertEqual(user.username, updated.username)
        self.assertTrue(user.check_password('catdog'))
