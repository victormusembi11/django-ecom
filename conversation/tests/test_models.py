from django.contrib.auth.models import User
from django.test import TestCase

from item.models import Item, Category
from conversation.models import Conversation, ConversationMessage


class ConversationModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.category = Category.objects.create(name="Test Category")
        self.item = Item.objects.create(
            name="Test Item",
            description="Test Description",
            price=10.0,
            created_by=self.user,
            category=self.category,
        )

    def test_conversation_creation(self):
        conversation = Conversation.objects.create(item=self.item)
        self.assertTrue(isinstance(conversation, Conversation))
        self.assertEqual(conversation.item, self.item)

    def test_conversation_members(self):
        conversation = Conversation.objects.create(item=self.item)
        conversation.members.add(self.user)

        self.assertEqual(conversation.members.count(), 1)
        self.assertIn(self.user, conversation.members.all())

    def test_conversation_message_creation(self):
        conversation = Conversation.objects.create(item=self.item)

        message = ConversationMessage.objects.create(
            conversation=conversation, content="Test Message", created_by=self.user
        )

        self.assertTrue(isinstance(message, ConversationMessage))
        self.assertEqual(message.conversation, conversation)
        self.assertEqual(message.content, "Test Message")
        self.assertEqual(message.created_by, self.user)
