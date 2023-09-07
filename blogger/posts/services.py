from core.utils import model_update
from posts.models import Post
from users.models import User


def post_create(text: str, author: User) -> Post:
    post = Post(text=text, author=author)
    post.full_clean()
    post.save()
    return post


def post_update(post: Post, **data) -> Post:
    return model_update(post, **data)
