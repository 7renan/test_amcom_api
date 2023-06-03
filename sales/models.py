from django.db import models


# models
from customers.models import Customer

class Saler(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class Sale(models.Model):
    invoice = models.IntegerField()
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    saler = models.ForeignKey(Saler, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.invoice)