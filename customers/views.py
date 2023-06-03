from django.shortcuts import render
from rest_framework import viewsets

# models
from customers.models import Customer

# serializers
from customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
