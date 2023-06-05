from rest_framework import serializers

# models
from sales.models import Sale, Saler, ItemSale

# serilizers
from products.serializers import ProductSerializer
from customers.serializers import CustomerSerializer

class SalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saler
        fields = ['id', 'name', 'email', 'phone']

class ItemSaleSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True, many=False)
    class Meta:
        model = ItemSale
        fields = ['id', 'product', 'amount']

class SaleDetailSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    saler = SalerSerializer(read_only=True)
    products = ItemSaleSerializer(many=True)

    class Meta:
        model = Sale
        fields = ['id', 'invoice', 'date', 'customer', 'saler', 'products']



class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ['id', 'invoice', 'date', 'customer', 'saler', 'products']




class ComissionSerializer(serializers.ModelSerializer):
    saler = SalerSerializer(read_only=True)
    total_commissions = serializers.DecimalField(max_digits=9, decimal_places=2)
