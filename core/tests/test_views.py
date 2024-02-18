from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from item.models import Category, Item


class CoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="password"
        )
        self.category = Category.objects.create(name="Test Category")
        self.item1 = Item.objects.create(
            name="Item 1",
            price=10.0,
            is_sold=False,
            category=self.category,
            created_by=self.user,
            image="test_image.jpg",
        )
        self.item2 = Item.objects.create(
            name="Item 2",
            price=20.0,
            is_sold=False,
            category=self.category,
            created_by=self.user,
            image="test_image.jpg",
        )

    def test_index_view(self):
        response = self.client.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/index.html")
        self.assertTrue("items" in response.context)
        self.assertTrue("categories" in response.context)
        self.assertEqual(len(response.context["items"]), 2)
        self.assertEqual(len(response.context["categories"]), 1)

    def test_contact_view(self):
        response = self.client.get(reverse("core:contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/contact.html")

    def test_signup_view(self):
        response = self.client.get(reverse("core:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/signup.html")

    def test_signup_post_view(self):
        data = {
            "username": "markdoe",
            "email": "markdoe@example.com",
            "password1": "md@123*!!",
            "password2": "md@123*!!",
        }
        response = self.client.post(reverse("core:signup"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="markdoe").exists())
