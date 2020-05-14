from django.test import TestCase
from django.template import Template, Context

from .blog_factories import PostFactory


class CustomTemplateTagTest(TestCase):

    TEMPLATE_WITH_TOTAL_POST = Template(
        "{% load blog_tags %} {% total_posts %}")
    TEMPLATE_WITH_LATEST_POST = Template(
        "{% load blog_tags %} {% show_latest_posts %}")
    TEMPLATE_WITH_MOST_COMMENTED_POST = Template(
        "{% load blog_tags %} {% get_most_commented_posts %}")

    def test_total_post(self):
        PostFactory.create_batch(5)
        rendered = self.TEMPLATE_WITH_TOTAL_POST.render(Context({}))

        self.assertIn('5', rendered)

    def test_show_latest_post(self):
        posts = PostFactory.create_batch(5)

        rendered = self.TEMPLATE_WITH_LATEST_POST.render(Context({}))

        self.assertIn(posts[0].title, rendered)
        self.assertIn(posts[4].title, rendered)

    def test_get_most_commented_posts(self):
        posts = PostFactory.create_batch(5)
        rendered = self.TEMPLATE_WITH_MOST_COMMENTED_POST.render(Context({}))

        self.assertIn(posts[0].title, rendered)
        self.assertIn(posts[4].title, rendered)
