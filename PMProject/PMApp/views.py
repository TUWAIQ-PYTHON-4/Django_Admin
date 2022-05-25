
from PMApp.models import Task


def lst():
    Task.objects.all()
    context = {"key1": "value", "key2": "value"}
    return context
