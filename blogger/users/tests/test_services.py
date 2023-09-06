from django.test import TestCase

from users import services
from users.models import User


class TestServices(TestCase):
    def test_user_create_service(self):
        self.assertEqual(0, User.objects.count())
        user = services.user_create(
            'bob@example.com', 'bob', 'testpass123',
        )
        self.assertEqual(1, User.objects.count())
        self.assertEqual(user, User.objects.first())
