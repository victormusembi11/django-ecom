"""This file is used to configure the app name for the dashboard app."""

from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """Dashboard app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "dashboard"
