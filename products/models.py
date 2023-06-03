from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    code = models.IntegerField()
    description = models.TextField()
    value_unit = models.DecimalField(decimal_places=2, max_digits=9)
    commission = models.DecimalField(decimal_places=2, max_digits=9, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return str(self.code)
