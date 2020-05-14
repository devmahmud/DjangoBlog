from django.test import TestCase
from django.core import mail

from blog.forms import CommentForm, EmailPostForm
from .blog_factories import PostFactory


class BlogFormTests(TestCase):
    """
    Test class for blog Forms
    """

    def test_comment_form_with_invalid_data(self):
        """
        Test comment form with invalid data
        """
        form = CommentForm({
            'name': 'John Doe',
            'email': 'Invalid Email'
        })
        self.assertFalse(form.is_valid())

    def test_comment_form_with_valid_data(self):
        """
        Test comment form with valid data
        """
        form = CommentForm({
            'name': 'John Doe',
            'email': 'johndoe@gmail.com',
            'body': 'Some Comment'
        })
        self.assertTrue(form.is_valid())

    def test_comment_saved_into_database(self):
        """
        Test valid comment is saving into database
        """
        form = CommentForm({
            'name': 'John Doe',
            'email': 'johndoe@gmail.com',
            'body': 'Some Comment'
        })
        comment = form.save(commit=False)
        comment.post = PostFactory()
        self.assertEqual(comment.name, 'John Doe')
        self.assertEqual(comment.email, 'johndoe@gmail.com')
        self.assertEqual(comment.body, 'Some Comment')

    def test_email_post_form_with_invaild_data(self):
        """
        Test email post form with invalid data
        """
        form = EmailPostForm({
            'name': 'John Doe',
            'email': 'invalidemail',
            'to': 'invalidemail'
        })
        self.assertFalse(form.is_valid())

    def test_email_post_form_with_vaild_data(self):
        """
        Test email post form with valid data
        """
        form = EmailPostForm({
            'name': 'John Doe',
            'email': 'jdoe@gmail.com',
            'to': 'missdoe@gmail.com',
            'comments': 'some comments'
        })
        self.assertTrue(form.is_valid())

    def test_send_email_with_email_post_form(self):
        """
        Test sharing post with EmailPostForm
        """
        post = PostFactory.create()

        form = EmailPostForm({
            'name': 'John Doe',
            'email': 'jdoe@gmail.com',
            'to': 'missdoe@gmail.com',
            'comments': 'some comments'
        })

        post_url = post.get_absolute_url()

        if form.is_valid():
            cd = form.cleaned_data
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                f"{cd['name']}\'s comments: {cd['comments']}"
            mail.send_mail(subject, message, 'admin@myblog.com', [cd['to']])

            self.assertEqual(len(mail.outbox), 1)
            self.assertEqual(mail.outbox[0].subject, subject)
        else:
            self.assertTrue(form.is_valid)
