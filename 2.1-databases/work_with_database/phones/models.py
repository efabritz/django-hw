from django.db import models
from datetime import date


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=500)
    release_date = models.DateField(default=date.today)
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=20)
