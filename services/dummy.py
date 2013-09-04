from tasks.models import Task
from .base import library


@library.register('dummy')
def dummy_service(data):
    """Create task from data dict"""
    Task.objects.create_task(data)
