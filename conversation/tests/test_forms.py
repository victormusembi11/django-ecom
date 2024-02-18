"""Test the forms of the conversation app."""

from django.test import TestCase

from conversation.forms import ConversationMessageForm


class ConversationMessageFormTest(TestCase):
    """Test the ConversationMessageForm."""

    def test_valid_form(self):
        """Test valid form submission."""
        form_data = {"content": "Test message content"}
        form = ConversationMessageForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test invalid form submission."""
        form_data = {"content": ""}
        form = ConversationMessageForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_widget_attrs(self):
        """Test the widget attributes of the form fields."""
        form = ConversationMessageForm()
        self.assertIn(
            'class="w-full py-4 px-6 rounded-xl border"', str(form["content"])
        )
