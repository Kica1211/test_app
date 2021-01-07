from django.db import models

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    pub_date = models.DateTimeField('Time to')

    def __str__(self):
        return self.title
