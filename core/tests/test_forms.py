"""Test cases for the forms in the core app."""

from django.test import TestCase
from django.contrib.auth.models import User

from core.forms import LoginForm, SignupForm


class LoginFormTestCase(TestCase):
    """Test cases for the login form."""

    def test_login_form_rendering(self):
        """Test the rendering of the login form."""
        form = LoginForm()
        self.assertIn('placeholder="Your username"', form.as_p())
        self.assertIn('placeholder="Your password"', form.as_p())
        self.assertIn('class="w-full py-4 px-6 rounded-xl"', form.as_p())

    def test_login_form_validation(self):
        """Test the validation of the login form."""
        User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        form_data = {"username": "testuser", "password": "testpassword"}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {"username": "testuser", "password": "wrongpassword"}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())


class SignupFormTestCase(TestCase):
    """Test cases for the signup form."""

    def test_signup_form_rendering(self):
        """Test the rendering of the signup form."""
        form = SignupForm()
        self.assertIn('placeholder="Your username"', form.as_p())
        self.assertIn('placeholder="Your email address"', form.as_p())
        self.assertIn('placeholder="Your password"', form.as_p())
        self.assertIn('placeholder="Repeat password"', form.as_p())
        self.assertIn('class="w-full py-4 px-6 rounded-xl"', form.as_p())

    def test_signup_form_validation(self):
        """Test the validation of the signup form."""
        form_data = {
            "username": "marcusrashford",
            "email": "marcusrashford@example.com",
            "password1": "mr@123*!!",
            "password2": "mr@123*!!",
        }
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

        form_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "newpassword",
            "password2": "differentpassword",
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())

        User.objects.create_user(
            username="existinguser",
            email="existinguser@example.com",
            password="existingpassword",
        )
        form_data = {
            "username": "existinguser",
            "email": "newuser@example.com",
            "password1": "newpassword",
            "password2": "newpassword",
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
