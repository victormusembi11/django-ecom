from django.test import TestCase

from conversation.forms import ConversationMessageForm


class ConversationMessageFormTest(TestCase):
    def test_valid_form(self):
        # Create form data
        form_data = {"content": "Test message content"}

        # Instantiate the form with the form data
        form = ConversationMessageForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Create form data with invalid content (empty in this case)
        form_data = {"content": ""}

        # Instantiate the form with the form data
        form = ConversationMessageForm(data=form_data)

        # Check if the form is not valid
        self.assertFalse(form.is_valid())

    def test_form_widget_attrs(self):
        # Instantiate the form
        form = ConversationMessageForm()

        # Check if the 'content' field has the expected widget attributes
        self.assertIn(
            'class="w-full py-4 px-6 rounded-xl border"', str(form["content"])
        )
