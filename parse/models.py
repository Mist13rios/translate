from django.db import models

# Create your models here.
VAL_LIST = (
    ('dollar', '$'),
)

class DayHistory(models.Model):

    date = models.CharField(max_length=64, blank=False)
    price = models.CharField(max_length=64, blank=False)
    open = models.CharField(max_length=64, blank=False)
    high = models.CharField(max_length=64, blank=False)
    low = models.CharField(max_length=64, blank=False)
    change = models.CharField(max_length=64, blank=False)
    val = models.CharField(choices=VAL_LIST, max_length=64, blank=True, null=True, default='dollar')