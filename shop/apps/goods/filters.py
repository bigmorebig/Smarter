__author__ = 'xiao tang'
__date__ = '2019/3/20 20:46'

import django_filters
from django.db.models import Q
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.filters.NumberFilter(field_name="shop_price", help_text='最大值', lookup_expr='gte')
    pricemax = django_filters.filters.NumberFilter(field_name="shop_price", help_text='最小值', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) |
                               Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
