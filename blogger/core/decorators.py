from functools import wraps
from typing import Callable

from rest_framework.serializers import BaseSerializer
from rest_framework.response import Response


def input(schema: BaseSerializer, partial: bool = False):
    """
    Input settings for view.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            s = schema(data=request.data, partial=partial)
            s.is_valid(raise_exception=True)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def output(
    schema: BaseSerializer, 
    many: bool = False, 
    status: int = 200
):
    """
    Output settings for view.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            result = func(request, *args, **kwargs)
            s = schema(result, many=many)
            return Response(s.data, status=status)
        return wrapper
    return decorator
