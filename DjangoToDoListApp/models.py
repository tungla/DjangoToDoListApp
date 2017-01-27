from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class ToDoItem(models.Model):
    item_text = models.CharField(max_length=100)
    created_date = models.DateTimeField('Date Created')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.item_text