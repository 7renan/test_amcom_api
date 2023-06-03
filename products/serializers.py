from rest_framework import serializers

# models
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['code', 'description', 'value_unit', 'commission']
