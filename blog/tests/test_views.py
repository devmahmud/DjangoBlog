from django.test import TestCase
from django.urls import reverse

from .blog_factories import PostFactory

POST_LIST_URL = reverse('blog:post_list')
POST_LIST_BY_TAG_URL = 'blog:post_list_by_tag'
POST_SHARE_URL = 'blog:post_share'
POST_FEED_URL = reverse('blog:post_feed')


class BlogViewTests(TestCase):
    """
    Test class for blog Views
    """

    def test_post_list_view(self):
        """
        Test post_list view
        """
        response = self.client.get(POST_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Blog Posts')
        self.assertTemplateUsed(response, 'blog/post-list.html')

    def test_post_detail_view(self):
        """
        Test for post detail view
        """
        post = PostFactory.create()
        response = self.client.get(post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertTemplateUsed(response, 'blog/post-detail.html')

    def test_post_list_by_tag_view(self):
        """
        Test for post list views by tag view
        """
        post = PostFactory.create()
        tag = post.tags.first()
        response = self.client.get(
            reverse(POST_LIST_BY_TAG_URL, kwargs={'tag_slug': tag}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertTemplateUsed(response, 'blog/post-list.html')

    def test_post_share_view(self):
        """
        Test for post share view
        """
        post = PostFactory.create()
        response = self.client.get(
            reverse(POST_SHARE_URL, kwargs={'post_id': post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertTemplateUsed(response, 'blog/post-share.html')

    def test_post_feed_view(self):
        """
        Test for post feed view
        """
        response = self.client.get(POST_FEED_URL)
        self.assertEqual(response.status_code, 200)

    def test_sitemap_view(self):
        """
        Test for sitemap view
        """
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        """
        Test for search view
        """
        post = PostFactory.create()
        response = self.client.get(
            POST_LIST_URL+"?query={0}".format(post.title))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)
        self.assertTemplateUsed(response, 'blog/post-list.html')
