from rest_framework import routers

api_routers = routers.DefaultRouter()

# views
from customers.views import CustomerViewSet
from products.views import ProductViewSet
from sales.views import SalerViewSet, SaleViewSet, ItemSaleViewSet

# register routes
api_routers.register('customers', CustomerViewSet)
api_routers.register('products', ProductViewSet)
api_routers.register('salers', SalerViewSet)
api_routers.register('sales', SaleViewSet)
api_routers.register('item-sale', ItemSaleViewSet)