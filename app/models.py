from django.contrib.postgres.fields import JSONField
from django.db import models


class Example(models.Model):
    data = JSONField(null=True, blank=True)
