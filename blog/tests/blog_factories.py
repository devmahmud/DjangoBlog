import factory
import factory.fuzzy
from django.contrib.auth import get_user_model

from blog.models import Post, Comment


User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    """
    Factory for user
    """
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.PostGenerationMethodCall(
        'set_password', factory.Faker('password')
    )


class PostFactory(factory.DjangoModelFactory):
    """
    Factory For Post
    """
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    slug = factory.Faker('slug')
    author = factory.SubFactory(UserFactory)
    body = factory.Faker('text')
    image = factory.django.ImageField(
        color=factory.fuzzy.FuzzyChoice(['blue', 'yellow', 'green', 'orange']),
        height=720,
        width=1280,
    )
    status = "published"

    @factory.post_generation
    def post_tags(self, create, extracted, **kwargs):
        for _ in range(3):
            self.tags.add(factory.Faker('word').generate())


class CommentFactory(factory.DjangoModelFactory):
    """
    Factory For Comment
    """
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    name = factory.Faker('name')
    email = factory.Faker('email')
    body = factory.Faker('text')
