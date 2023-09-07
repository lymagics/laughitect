from rest_framework import serializers

from posts.models import Post
from users.api.schemas import UserOut


class PostIn(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('text',)


class PostOut(serializers.ModelSerializer):
    author = UserOut()

    class Meta:
        model = Post
        fields = ('id', 'text', 'created_at', 'author',)
