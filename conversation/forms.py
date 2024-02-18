"""Forms for the conversation app."""

from django import forms

from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    """Form for creating a new conversation message."""

    class Meta:
        """Meta options for the form."""

        model = ConversationMessage
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            )
        }
