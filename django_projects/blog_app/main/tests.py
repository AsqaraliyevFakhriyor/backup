from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.
class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@mail.ru",
            password="secretpassword"
        )

        self.post = Post.objects.create(
            title="test post",
            body="this is test post with author",
            author=self.user
        )


    def test_string_representation(self):
        post = Post(title="test post")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "test post")
        self.assertEqual(f"{self.post.body}", "this is test post with author")
        self.assertEqual(f"{self.post.author}", "testuser")

    def test_post_list_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test post")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("/post/1/")
        no_response = self.client.get("/post/1000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "test post")
        self.assertTemplateUsed("post_detail.html")