from datetime import datetime
import decimal
from django.db.models import Sum, F, Q, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Cast
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# models
from sales.models import Sale, Saler, ItemSale

# serializers
from sales.serializers import SaleSerializer, SalerSerializer, ItemSaleSerializer, ComissionSerializer


class SalerViewSet(viewsets.ModelViewSet):
    queryset = Saler.objects.all()
    serializer_class = SalerSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    @action(detail=False, methods=['GET'])
    def comissions(self, request):
        date_init = request.query_params.get('date_init', False)
        date_final = request.query_params.get('date_final', False)

        if date_init and date_final:
            date_init = datetime.strptime(request.query_params.get('date_init'), "%Y-%m-%d")
            date_final = datetime.strptime(request.query_params.get('date_final'), "%Y-%m-%d")
            queryset = Sale.objects.filter(Q(date__gte=date_init) & Q(date__lte=date_final))
            comissions = queryset.values('saler').annotate(
                total_comission=
                    Sum(F('products__product__value_unit') * (F('products__product__commission') / 100.00), output_field=DecimalField()),
                name=F('saler__name'),
                total_salers=Count('saler')
            )
            return Response(comissions, status=status.HTTP_200_OK)
        return Response({'Erro': 'É necessário passar um intervalo de datas válidas'},
                        status=status.HTTP_400_BAD_REQUEST)


class ItemSaleViewSet(viewsets.ModelViewSet):
    queryset = ItemSale.objects.all()
    serializer_class = ItemSaleSerializer
