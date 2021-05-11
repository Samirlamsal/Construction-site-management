import django_filters
from .models import Transaction
from django_filters import DateFilter


class TransactionFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="trans_date", lookup_expr='gte')

    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['amount', 'trans_method', 'trans_date', 'comments']
