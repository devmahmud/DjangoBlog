from django.test import TestCase
from blog.models import Post, Comment

from .blog_factories import PostFactory, CommentFactory


class BlogModelTests(TestCase):
    """
    Test class for blog models
    """

    def test_creating_post(self):
        """
        Test creating Post model object
        """
        post = PostFactory.create()
        model_post = Post.objects.get(id=post.id)

        self.assertEqual(post.id, model_post.id)
        self.assertEqual(post.title, model_post.title)
        self.assertEqual(post.author, model_post.author)
        self.assertEqual(post.image, model_post.image)
        self.assertEqual(post.publish, model_post.publish)
        self.assertEqual(post.created, model_post.created)
        self.assertEqual(post.updated, model_post.updated)
        self.assertEqual(post.status, model_post.status)
        self.assertEqual(post.tags, model_post.tags)

    def test_post_string_representation(self):
        """
        Test string representation of Post object
        """
        post = PostFactory.create()
        self.assertEqual(str(post), post.title)

    def test_creating_commnet(self):
        """
        Test creating Comment model object
        """
        comment = CommentFactory.create()
        model_comment = Comment.objects.get(id=comment.id)

        self.assertEqual(comment.id, model_comment.id)
        self.assertEqual(comment.name, model_comment.name)
        self.assertEqual(comment.email, model_comment.email)
        self.assertEqual(comment.body, model_comment.body)

    def test_comment_string_representation(self):
        """
        Test string representation of Comment object
        """
        comment = CommentFactory.create()
        self.assertEqual(
            str(comment), f'Comment by {comment.name} on {comment.post}')
