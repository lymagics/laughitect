from django.http import Http404

from auth.authentication import JWTAuthentication
from core.decorators import input, output
from posts import selectors, services
from posts.api.schemas import PostIn, PostOut
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@output(PostOut)
def post_get(request, pk: int):
    post = selectors.post_get(pk)
    if post is None:
        raise Http404
    return post


@api_view(['GET'])
@output(PostOut, many=True)
def post_list(request):
    return selectors.post_list()


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@input(PostIn)
@output(PostOut)
def post_create(request):
    data = request.data
    post = services.post_create(
        data['text'], request.user,
    )
    return post


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@input(PostIn, partial=True)
@output(PostOut)
def post_update(request, pk: int):
    data = request.data
    post = selectors.post_get(pk)
    if post is None:
        raise Http404
    if post.author != request.user:
        detail = {'detail': 'Not your post.'}
        return Response(detail, status=403)
    post = services.post_update(post, **data)
    return post


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_delete(request, pk: int):
    post = selectors.post_get(pk)
    if post is None:
        raise Http404
    if post.author != request.user:
        detail = {'detail': 'Not your post.'}
        return Response(detail, status=403)
    services.post_delete(post)
    return Response(status=204)
