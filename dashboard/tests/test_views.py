from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from item.models import Item, Category


class DashboardViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Test Category")
        self.item1 = Item.objects.create(
            name="Test Item 1",
            description="Description for Test Item 1",
            price=10.0,
            category=self.category,
            created_by=self.user,
            image="test_image.jpg",
        )
        self.item2 = Item.objects.create(
            name="Test Item 2",
            description="Description for Test Item 2",
            price=20.0,
            category=self.category,
            created_by=self.user,
            image="test_image.jpg",
        )

    def test_index_view_authenticated_user(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("dashboard:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/index.html")
        self.assertContains(response, "Test Item 1")
        self.assertContains(response, "Test Item 2")

    def test_index_view_unauthenticated_user(self):
        response = self.client.get(reverse("dashboard:index"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/dashboard/")
