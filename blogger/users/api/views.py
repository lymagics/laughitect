from django.http import Http404

from auth.authentication import JWTAuthentication
from core.decorators import input, output
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users import selectors, services
from users.api.schemas import UserIn, UserOut
from users.errors import FollowError


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
def user_get(request, pk: int):
    user = selectors.user_get(pk)
    if user is None:
        raise Http404
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
    data = request.data
    services.user_update(
        request.user, **data
    )
    return Response(status=200)


@api_view(['GET'])
@output(UserOut, many=True)
def user_list(request):
    return selectors.user_list()


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_follow(request, pk: int):
    user = selectors.user_get(pk)
    if user is None:
        raise Http404
    try:
        services.user_follow(
            request.user, user,
        )
        return Response(status=200)
    except FollowError as e:
        detail = {'detail': str(e)}
        return Response(detail, status=400)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_unfollow(request, pk: int):
    user = selectors.user_get(pk)
    if user is None:
        raise Http404
    try:
        services.user_unfollow(
            request.user, user,
        )
        return Response(status=200)
    except FollowError as e:
        detail = {'detail': str(e)}
        return Response(detail, status=400)


@api_view(['GET'])
@output(UserOut, many=True)
def user_following(request, pk: int):
    user = selectors.user_get(pk)
    if user is None:
        raise Http404
    following = selectors.user_following(user)
    return following


@api_view(['GET'])
@output(UserOut, many=True)
def user_followers(request, pk: int):
    user = selectors.user_get(pk)
    if user is None:
        raise Http404
    followers = selectors.user_followers(user)
    return followers
