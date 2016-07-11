from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()

    def __str__(self):
        return "{0}: {1} calories".format(self.name, self.calories)

