from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from item.models import Category, Item


class ConversationViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="password"
        )
        self.other_user = User.objects.create_user(
            username="otheruser", email="other@example.com", password="password"
        )
        self.category = Category.objects.create(name="Test Category")
        self.item = Item.objects.create(
            name="Test Item",
            price=10.0,
            is_sold=False,
            category=self.category,
            created_by=self.other_user,
            image="test_image.jpg",
        )

    def test_new_conversation_view_POST(self):
        data = {"content": "Test message"}
        response = self.client.post(
            reverse("conversation:new", kwargs={"item_pk": self.item.id}), data
        )
        self.assertEqual(response.status_code, 302)
