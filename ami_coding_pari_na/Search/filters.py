from .models import Search
from django_filters import rest_framework as filters

class SearchResultFilter(filters.FilterSet):
    start_date = filters.DateTimeFilter(
            field_name="timestamp", lookup_expr='date__gte')
    end_date = filters.DateTimeFilter(
            field_name="timestamp", lookup_expr='date__lte')

    class Meta:
        model = Search
        fields = ['user_id' ,'start_date', 'end_date']