from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Post


class BlogViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test')
        self.live_post = self.create_post()
        self.draft_post = self.create_post(title='Draft Post',
            published=False)

    def create_post(self, title='Test Blog Post', published=True):
        return Post.objects.create(
            title=title,
            author=self.user,
            published=published
        )

    def test_list_view(self):
        url = reverse('blog:list')
        req = self.client.get(url)
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'blog/post_list.html')
        self.assertIn(self.live_post.title, req.rendered_content)
        self.assertIn(self.live_post.get_absolute_url(),
            req.rendered_content)

    def test_detail_view(self):
        url = reverse('blog:detail',
            kwargs={'slug': self.live_post.slug})
        req = self.client.get(url)
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'blog/post_detail.html')
        self.assertIn(self.live_post.title, req.rendered_content)
        self.assertIn(reverse('blog:list'), req.rendered_content)

    def test_draft_view(self):
        url = self.draft_post.get_absolute_url()
        req = self.client.get(url)
        self.assertEqual(req.status_code, 404)
