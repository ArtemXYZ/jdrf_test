from django.db import models


# ----------------------------------------------------------------------------------------------------------------------
class Task(models.Model):

    title = models.CharField(max_length=100, blank=False)
    is_completed = models.BooleanField(default=False)

    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title}, is_completed={self.is_completed}).'

    def __str__(self):
        return self.title
