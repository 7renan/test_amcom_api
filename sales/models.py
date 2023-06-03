from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# models
from customers.models import Customer
from products.models import Product


class Saler(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


class ItemSale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'código do produto: {self.product}'

    class Meta:
        verbose_name = 'Item de venda'
        verbose_name_plural = 'Items ded vendas'


class Sale(models.Model):
    invoice = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    saler = models.ForeignKey(Saler, on_delete=models.CASCADE)
    products = models.ManyToManyField(ItemSale)

    def __str__(self):
        return f'Número da nota fiscal: {str(self.invoice)}'

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'


class DaysWeekConfig(models.Model):
    day = models.CharField(max_length=100)
    min_comission = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(10)], max_digits=5,
                                        decimal_places=2)
    max_comission = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(10)], max_digits=5,
                                        decimal_places=2)

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = 'Comissão dia da semana'
        verbose_name_plural = 'Comissões dias da semana'
