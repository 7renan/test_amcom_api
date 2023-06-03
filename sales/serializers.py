from rest_framework import serializers

# models
from sales.models import Sale, Saler, ItemSale


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

    class Meta:
        model = ItemSale
        fields = ['product', 'amount']
