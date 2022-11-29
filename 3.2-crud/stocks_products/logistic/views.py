from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['^products__title', '^products__description']
    filterset_fields = ['products']

#
# 2
# обновляем записи на складе ---
# PATCH {{baseUrl}}/stocks/4/
# Content-Type: application/json
#
# {
#   "positions": [
#     {
#       "product": 2,
#       "quantity": 100,
#       "price": 130.80
#     },
#     {
#       "product": 3,
#       "quantity": 243,
#       "price": 145
#     }
#   ]
# }
# 2 подряд делает list concatination вместо обновления