from posts.models import Post


def post_get(post_id: int) -> Post:
    return Post.objects.filter(pk=post_id).first()
