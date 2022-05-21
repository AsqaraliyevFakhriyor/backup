from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Todo

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_main_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


    def test_about_page(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)

    def test_404_url(self):
        response = self.client.get("/vapshemmalades")
        self.assertEqual(response.status_code, 404)

class TodoModelTest(TestCase):
    def setUp(self):
        Todo.objects.create(title="django it is", description="this is description for django it is!")

    def test_description_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_title = str(todo.title)
        expected_object_description = str(todo.description)
        self.assertEqual(expected_object_title, "django it is")
        self.assertEqual(expected_object_description, "this is description for django it is!")
