import django_filters
from .models import ProductModel


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name='product_price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(
        field_name='product_price', lookup_expr='lte')

    class Meta:
        model = ProductModel
        fields = ['min_price', 'max_price']
