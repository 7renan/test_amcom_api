from rest_framework import serializers

# models
from sales.models import Sale, Saler, ItemSale
from products.serializers import ProductSerializer


class SaleSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=ItemSale.objects.all(), many=True)

    class Meta:
        model = Sale
        fields = ['invoice', 'date', 'customer', 'saler', 'products']


class SalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saler
        fields = ['name', 'email', 'phone']


class ItemSaleSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True, many=False)
    class Meta:
        model = ItemSale
        fields = ['product', 'amount']

class ComissionSerializer(serializers.ModelSerializer):
    saler = SalerSerializer(read_only=True)
    total_commissions = serializers.DecimalField(max_digits=9, decimal_places=2)
