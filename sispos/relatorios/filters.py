import django_filters
from sispos.relatorios.models import Relatorios


class RelatoriosFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter('Nome')
    orientador = django_filters.CharFilter('Orientador')
    created = django_filters.DateFilter('Envio')

    class Meta:
        model = Relatorios
        fields = ['nome', 'orientador', 'created']