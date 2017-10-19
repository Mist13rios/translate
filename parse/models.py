from django.db import models

# Create your models here.
VAL_LIST = (
    ('dollar', '$'),
)

class DayHistory(models.Model):

    date = models.CharField(max_length=64, blank=False)
    price = models.DecimalField(blank=False, max_digits=5, decimal_places=1)
    open = models.DecimalField(blank=False, max_digits=5, decimal_places=1)
    high = models.DecimalField(blank=False, max_digits=5, decimal_places=1)
    low = models.DecimalField(blank=False, max_digits=5, decimal_places=1)
    change = models.DecimalField(blank=False, max_digits=4, decimal_places=2)
    val = models.CharField(choices=VAL_LIST, max_length=64, blank=True, null=True, default='dollar')