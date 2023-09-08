from users.models import User


def user_get(user_id: int) -> User:
    return User.objects.filter(pk=user_id).first()


def user_list() -> list[User]:
    return User.objects.all()
