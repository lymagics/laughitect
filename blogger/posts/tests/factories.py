import factory
from factory.django import DjangoModelFactory
from posts.models import Post
from users.tests.factories import UserFactory


class PostFactory(DjangoModelFactory):
    text = factory.Faker('sentence')
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Post
