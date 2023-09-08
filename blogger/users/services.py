from core.utils import model_update
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
