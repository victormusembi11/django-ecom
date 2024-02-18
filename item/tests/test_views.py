from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from item.models import Category, Item
from item.forms import NewItemForm, EditItemForm


class ItemViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")
        self.category = Category.objects.create(name="Test Category")
        self.item = Item.objects.create(
            name="Test Item",
            category=self.category,
            price=10.0,
            created_by=self.user,
            image="test_image.jpg",
        )

    def test_items_view(self):
        response = self.client.get(reverse("item:items"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "item/items.html")

    def test_detail_view(self):
        response = self.client.get(reverse("item:detail", kwargs={"pk": self.item.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "item/detail.html")

    def test_new_view_GET(self):
        response = self.client.get(reverse("item:new"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "item/form.html")
        self.assertIsInstance(response.context["form"], NewItemForm)

    def test_new_view_POST(self):
        image = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg"
        )
        form_data = {
            "category": self.category.id,
            "name": "New Test Item",
            "description": "New Test Description",
            "price": 15.0,
            "image": image,
        }
        response = self.client.post(reverse("item:new"), form_data)
        self.assertEqual(response.status_code, 200)

    def test_edit_view_GET(self):
        response = self.client.get(reverse("item:edit", kwargs={"pk": self.item.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "item/form.html")
        self.assertIsInstance(response.context["form"], EditItemForm)

    def test_edit_view_POST(self):
        form_data = {
            "name": "Edited Test Item",
            "description": "Edited Test Description",
            "price": 20.0,
        }
        response = self.client.post(
            reverse("item:edit", kwargs={"pk": self.item.pk}), form_data
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_view(self):
        response = self.client.post(reverse("item:delete", kwargs={"pk": self.item.pk}))
        self.assertEqual(response.status_code, 302)
