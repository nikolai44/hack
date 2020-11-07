from django.conf import settings
from django.db import models
from django.utils import timezone


class FactureModel(models.Model):
    product_type = models.CharField(max_length=200)
    manufacture_name = models.CharField(max_length=200)
    weight = models.IntegerField()
    production_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.manufacture_name
