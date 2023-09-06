from django.contrib.auth import authenticate, login as django_login

from rest_framework.request import Request

from auth.errors import InvalidCredentials


def login(request: Request, username: str, password: str) -> str:
    user = authenticate(username=username, password=password)
    if user is None:
        error = 'Invalid username or password.'
        raise InvalidCredentials(error)
    django_login(request, user)
    return user.jwt_token
