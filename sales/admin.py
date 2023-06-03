from django.contrib import admin

# models
from sales.models import Saler, Sale, ItemSale, DaysWeekConfig

from django.db import models
from django.contrib import admin


class DaysWeekConfigAdmin(admin.ModelAdmin):
    list_display = ('day', 'min_comission', 'max_comission')


admin.site.register(Saler)
admin.site.register(Sale)
admin.site.register(ItemSale)
admin.site.register(DaysWeekConfig)
