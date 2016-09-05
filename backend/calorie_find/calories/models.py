from __future__ import unicode_literals
import logging

from django.db import models
from django.db.models import Lookup
from django.db.models.fields import CharField


# Create fuzzy match for pg_trgm extension
@CharField.register_lookup
class FuzzySearch(Lookup):
    lookup_name = "fuzzy"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return "{0} %% {1}".format(lhs, rhs), params


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()

    @classmethod
    def create(cls, name, calories):
        Food(name=name, calories=calories).save()

    def __str__(self):
        return "{0}: {1} calories".format(self.name, self.calories)



