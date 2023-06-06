from rest_framework import serializers

# models
from sales.models import Sale, Saler, ItemSale
from products.models import Product

# serilizers
from products.serializers import ProductSerializer
from customers.serializers import CustomerSerializer

class SalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saler
        fields = ['id', 'name', 'email', 'phone']

class ItemSaleSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False)
    class Meta:
        model = ItemSale
        fields = ['product', 'amount']

class SaleDetailSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    saler = SalerSerializer(read_only=True)
    products = ItemSaleSerializer(many=True)

    class Meta:
        model = Sale
        fields = ['id', 'invoice', 'date', 'customer', 'saler', 'products']



class SaleSerializer(serializers.ModelSerializer):

    products = ItemSaleSerializer(many=True)
    class Meta:
        model = Sale
        fields = ['id', 'invoice', 'date', 'customer', 'saler', 'products']

    def create(self, validated_data):  # Remove e obtém os dados dos produtos
        products_data = validated_data.pop('products')
        sale = Sale.objects.create(**validated_data)
        for product_data in products_data:
            product = Product.objects.create(**product_data['product'])
            item_product = ItemSale.objects.create(product=product, amount=product_data['amount'])
            sale.products.set([item_product])
        return sale

class ComissionSerializer(serializers.ModelSerializer):
    saler = SalerSerializer(read_only=True)
    total_commissions = serializers.DecimalField(max_digits=9, decimal_places=2)
