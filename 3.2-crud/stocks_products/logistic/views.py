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

# 1
# DELETE {{baseUrl}}/stocks/1
# Content-Type: application/json
# HTTP/1.1 301 Moved Permanently
# Date: Mon, 21 Nov 2022 13:35:43 GMT
# Server: WSGIServer/0.2 CPython/3.8.10
# Content-Type: text/html; charset=utf-8
# Location: /api/v1/stocks/1/
# Content-Length: 0
# X-Content-Type-Options: nosniff
# Referrer-Policy: same-origin
# Cross-Origin-Opener-Policy: same-origin

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