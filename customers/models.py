from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name
