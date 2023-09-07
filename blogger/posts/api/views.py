from django.http import Http404

from rest_framework.decorators import api_view

from core.decorators import output
from posts import selectors
from posts.api.schemas import PostOut


@api_view(['GET'])
@output(PostOut)
def post_get(request, pk: int):
    post = selectors.post_get(pk)
    if post is None:
        raise Http404
    return post
