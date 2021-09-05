from django.db import models


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=False, max_length=100)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
