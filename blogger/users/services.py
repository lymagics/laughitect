from core.utils import model_update
from users.errors import FollowError
from users.models import User


def user_create(
    email: str,
    username: str,
    password: str,
) -> User:
    user = User(email=email, username=username)
    user.set_password(password)
    user.full_clean()
    user.save()
    return user


def user_update(user: User, **data) -> User:
    user = model_update(user, **data)
    if 'password' in data:
        user.set_password(data['password'])
        user.save()
    return user


def user_follow(user: User, other: User):
    if user.is_following(other):
        error = 'You already follow this user.'
        raise FollowError(error)
    if user == other:
        error = 'You can\'t follow yourself.'
        raise FollowError(error)
    user.follow(other)


def user_unfollow(user: User, other: User):
    if not user.is_following(other):
        error = 'You don\'t follow this user.'
        raise FollowError(error)
    user.unfollow(other)
