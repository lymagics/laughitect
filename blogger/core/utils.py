from typing import Optional

from django.conf import settings

from rest_framework.response import Response

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
            algorithms=["HS256"],
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


def paginated_response(
    pagination_class,
    schema_class,
    queryset,
    request,
) -> Response:
    paginator = pagination_class()
    page = paginator.paginate_queryset(queryset, request)

    if page is not None:
        schema = schema_class(page, many=True)
        return paginator.get_paginated_response(schema.data)

    schema = schema_class(queryset, many=True)
    return Response(schema.data)
