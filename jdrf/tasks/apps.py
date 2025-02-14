from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        from .models import Task
        Task.objects.create(title="Забрать товар со склада", is_completed=False)