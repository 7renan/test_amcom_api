from django.shortcuts import render
from rest_framework import viewsets

# models
from sales.models import Sale, Saler, ItemSale

# serializers
from sales.serializers import SaleSerializer, SalerSerializer, ItemSaleSerializer


class SalerViewSet(viewsets.ModelViewSet):
    queryset = Saler.objects.all()
    serializer_class = SalerSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class ItemSaleViewSet(viewsets.ModelViewSet):
    queryset = ItemSale.objects.all()
    serializer_class = ItemSaleSerializer
