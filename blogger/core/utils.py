from typing import Optional

from django.conf import settings

import jwt


def encode_jwt(payload: dict) -> str:
    return jwt.encode(
        payload=payload,
        key=settings.SECRET_KEY,
        algorithm='HS256',
    )


def decode_jwt(jwt_token: str) -> Optional[dict]:
    try:
        return jwt.decode(
            jwt_token, 
            key=settings.SECRET_KEY, 
            algorithms=["HS256"]
        )
    except jwt.PyJWKError:
        return None


def model_update(instance, **data):
    for field in data:
        if hasattr(instance, field):
            setattr(instance, field, data[field])
    instance.full_clean()
    instance.save()
    return instance
