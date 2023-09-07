from django.http import Http404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from auth.authentication import JWTAuthentication
from core.decorators import input, output
from posts import selectors, services
from posts.api.schemas import PostIn, PostOut


@api_view(['GET'])
@output(PostOut)
def post_get(request, pk: int):
    post = selectors.post_get(pk)
    if post is None:
        raise Http404
    return post


@api_view(['GET'])
@output(PostOut,many=True)
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
