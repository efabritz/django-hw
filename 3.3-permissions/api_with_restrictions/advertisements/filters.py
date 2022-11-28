from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
        status = filters.ModelMultipleChoiceFilter(
                field_name="status",
                to_field_name="status",
                queryset=Advertisement.objects.all(),
        )
        created_at_after = filters.DateFilter(field_name='created_at', lookup_expr='gte')
        created_at_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')


        class Meta:
                model = Advertisement

                fields = ('status', 'created_at', 'updated_at')
                ordering = ('status', 'created_at', 'updated_at')