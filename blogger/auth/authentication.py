from core.utils import decode_jwt
from rest_framework import authentication
from rest_framework.request import Request
from users.selectors import user_get


class JWTAuthentication(authentication.BaseAuthentication):
    """
    JWT Authentication class.
    """
    def authenticate(self, request: Request):
        access = request.COOKIES.get('access')
        if access is None:
            return None

        payload = decode_jwt(access)
        if payload is None:
            return None

        user = user_get(payload['id'])
        return (user, None)
