from rest_framework.serializers import ModelSerializer
from users.models import User


class UserIn(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password',)


class UserOut(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username',)
