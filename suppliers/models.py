from django.conf import settings
from django.db import models
from django.utils import timezone


class FactureModel(models.Model):
    product_type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    years_active = models.IntegerField()
    factory_size = models.FloatField()
    farming_area = models.FloatField()
    total_carbon = models.FloatField()
    manufacture_name = models.CharField(max_length=200)
    meat_percentage = models.FloatField()
    fat_percentage = models.FloatField()
    weight = models.FloatField()
    production_date = models.DateTimeField(default=timezone.now)
    shelf_life_date = models.DateTimeField(blank=True, null=True)
    species = models.CharField(max_length=200)
    part = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    total_weight = models.FloatField()
    age = models.FloatField()
    antibiotics = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    carbon_footprint = models.FloatField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.manufacture_name


class GeodataModel(models.Model):
    uid = models.ForeignKey(FactureModel, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
