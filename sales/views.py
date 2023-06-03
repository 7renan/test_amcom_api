from django.shortcuts import render
from rest_framework import viewsets

# models
from sales.models import Sale, Saler

# serializers
from sales.serializers import SaleSerializer, SalerSerializer


class SalerViewSet(viewsets.ModelViewSet):
    queryset = Saler.objects.all()
    serializer_class = SalerSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
