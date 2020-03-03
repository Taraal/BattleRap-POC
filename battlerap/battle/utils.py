from datetime import timedelta
from django.utils import timezone


def get_timedelta(days):
    return timezone.now().date() - timedelta(days=days)