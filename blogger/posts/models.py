from django.conf import settings
from django.db import models

from core.models import BaseModel


class Post(BaseModel):
    """
    Post entity.
    """
    text = models.CharField(max_length=180)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='posts')

    def __str__(self) -> str:
        return self.text
