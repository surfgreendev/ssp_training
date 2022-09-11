from django.test import TestCase
from self_service_portal.blog.models import Post

# Create your tests here.
class PostModelTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test", sub_title="Test")

    def test_post_has_been_created(self):
        self.assertTrue(Post.objects.get(id=self.post.id))
        self.assertEqual(Post.objects.get(id=self.post.id).title, "Test")

    def test_if_status_set_to_published_published_on_is_added(self):
        self.post.status = "PUBLISHED"
        self.post.save()

        self.assertTrue(self.post.published_on)
        self.assertEqual(self.post.status, "PUBLISHED")
