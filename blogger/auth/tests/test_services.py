from unittest.mock import patch

from django.http import HttpRequest
from django.test import TestCase

from auth import services
from auth.errors import InvalidCredentials
from users.tests.factories import UserFactory


class TestServices(TestCase):
    @patch('auth.services.django_login')
    def test_login_service(self, django_login_mock):
        user = UserFactory()
        jwt_token = services.login(
            HttpRequest(), user.username, 'testpass123',
        )
        self.assertIsNotNone(jwt_token)

    @patch('auth.services.django_login')
    def test_login_service_fail(self, django_login_mock):
        with self.assertRaises(InvalidCredentials):
            services.login(
                HttpRequest(), 'bob', '123',
            )
