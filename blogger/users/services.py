from core.utils import model_update
from users.models import User
from users.selectors import user_get


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


def user_update(id: int, **data) -> User:
    user = user_get(id)
    user = model_update(user, **data)
    if 'password' in data:
        user.set_password(data['password'])
        user.save()
    return user
