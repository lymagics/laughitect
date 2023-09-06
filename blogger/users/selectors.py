from django.shortcuts import get_object_or_404

from users.models import User


def user_get(id: int):
    return get_object_or_404(User, pk=id)

