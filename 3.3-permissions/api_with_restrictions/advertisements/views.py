from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissons import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]
        return []


    @action(detail=False, methods=['get'], url_path='favs')
    def favs(self, request):
        new_queryset = []
        data = self.serializer_class.data
        qs = self.queryset
        for q in qs:
            user_id = request.user.id
            liked = q.liked.core_filters['likes__id']
            if user_id == liked:
                new_queryset.append(q)

        if len(new_queryset) == 0:
            return Response({"Error" : "Your favourite list is empty"})

        serializer = AdvertisementSerializer(new_queryset)
        return Response(serializer.data)
