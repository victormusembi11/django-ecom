from django.test import TestCase
from django.contrib.auth.models import User

from item.models import Category, Item


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="Test Category")

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field("name").max_length
        self.assertEqual(max_length, 255)

    def test_ordering(self):
        self.assertEqual(Category._meta.ordering, ("name",))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "Categories")


class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="testuser", password="12345")
        category = Category.objects.create(name="Test Category")
        Item.objects.create(
            category=category,
            name="Test Item",
            description="Test description",
            price=10.0,
            created_by=user,
        )

    def test_name_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_description_blank_null(self):
        item = Item.objects.get(id=1)
        field = item._meta.get_field("description")
        self.assertTrue(field.blank)
        self.assertTrue(field.null)

    def test_price_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field("price").verbose_name
        self.assertEqual(field_label, "price")

    def test_image_blank_null(self):
        item = Item.objects.get(id=1)
        field = item._meta.get_field("image")
        self.assertTrue(field.blank)
        self.assertTrue(field.null)

    def test_is_sold_default(self):
        item = Item.objects.get(id=1)
        self.assertFalse(item.is_sold)

    def test_created_by_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field("created_by").verbose_name
        self.assertEqual(field_label, "created by")

    def test_created_at_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field("created_at").verbose_name
        self.assertEqual(field_label, "created at")
