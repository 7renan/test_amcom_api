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
from sales.serializers import SaleSerializer, SalerSerializer, ItemSaleSerializer, ComissionSerializer, SaleDetailSerializer


class SalerViewSet(viewsets.ModelViewSet):
    queryset = Saler.objects.all()
    serializer_class = SalerSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SaleDetailSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = SaleDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def comissions(self, request):
        date_init = request.query_params.get('date_init', False)
        date_final = request.query_params.get('date_final', False)


        # validacao de params
        if date_init and date_final:
            date_init = datetime.strptime(request.query_params.get('date_init'), "%Y-%m-%d")
            date_final = datetime.strptime(request.query_params.get('date_final'), "%Y-%m-%d")
            # filtrando vendas pelo intervalo de datas
            queryset = Sale.objects.filter(Q(date__gte=date_init) & Q(date__lte=date_final))
            # agrupando as vendas pelo campo de vendedor e adicionando os campos: total comissions, name e total_salers
            comissions = queryset.values(saler_name=F('saler__name')).annotate(
                total_comission=
                    Sum(F('products__product__value_unit') * (F('products__product__commission') / 100.00), output_field=DecimalField()),
                total_sales=Count('products')
            )
            return Response(comissions, status=status.HTTP_200_OK)
        return Response({'Erro': 'É necessário passar um intervalo de datas válidas'},
                        status=status.HTTP_400_BAD_REQUEST)


class ItemSaleViewSet(viewsets.ModelViewSet):
    queryset = ItemSale.objects.all()
    serializer_class = ItemSaleSerializer
