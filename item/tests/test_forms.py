from django.contrib.auth.models import User
from django.test import TestCase

from item.forms import NewItemForm, EditItemForm
from item.models import Item, Category


class NewItemFormTest(TestCase):
    def test_valid_form_submission(self):
        category = Category.objects.create(name="Test Category")
        user = User.objects.create(username="testuser")
        data = {
            "category": category.id,
            "name": "Test Item",
            "description": "Test description",
            "price": 10.0,
        }
        form = NewItemForm(data=data)
        self.assertTrue(form.is_valid())


class EditItemFormTest(TestCase):
    def test_invalid_form_submission(self):
        invalid_data = {}
        category = Category.objects.create(name="Test Category")
        user = User.objects.create(username="testuser")
        item = Item.objects.create(
            name="Test Item", price=10.0, category=category, created_by=user
        )
        form = EditItemForm(instance=item, data=invalid_data)
        self.assertFalse(form.is_valid())

    def test_valid_form_submission(self):
        category = Category.objects.create(name="Test Category")
        user = User.objects.create(username="testuser")
        item = Item.objects.create(
            name="Test Item", price=10.0, category=category, created_by=user
        )
        data = {
            "name": "Updated Test Item",
            "description": "Updated description",
            "price": 20.0,
            "image": "test_image.jpg",
            "is_sold": True,
        }
        form = EditItemForm(instance=item, data=data)
        self.assertTrue(form.is_valid())
