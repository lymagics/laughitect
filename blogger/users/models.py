from django.contrib.auth.models import AbstractUser
from django.db import models

from core.utils import encode_jwt


class User(AbstractUser):
    """
    User entity.
    """
    email = models.EmailField()

    @property
    def jwt_token(self) -> str:
        payload = {'id': self.pk}
        return encode_jwt(payload)
