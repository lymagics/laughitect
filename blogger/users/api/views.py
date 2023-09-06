from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from auth.authentication import JWTAuthentication
from core.decorators import input, output
from users import services, selectors
from users.api.schemas import UserIn, UserOut


@api_view(['POST'])
@input(UserIn)
def user_create(request):
    data = request.data
    services.user_create(
        data['email'], data['username'], data['password'],
    )
    return Response(status=200)


@api_view(['GET'])
@output(UserOut)
def user_get(request, user_id: int):
    user = selectors.user_get(id=user_id)
    return user


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@output(UserOut)
def me(request):
    return request.user


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@input(UserIn, partial=True)
def user_update(request):
    user_id = request.user.pk
    data = request.data
    services.user_update(user_id, **data)
    return Response(status=200)
