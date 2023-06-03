from django.shortcuts import render
from rest_framework import viewsets

# models
from products.models import Product

# serializers
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
