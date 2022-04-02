"""Apps files."""

# Django
from django.apps import AppConfig


class OrdersConfig(AppConfig):  # noqa D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
