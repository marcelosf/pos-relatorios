import django_filters
from sispos.accounts.models import User


ORIENTADOR_GROUP_NAME = 'orientadores'


class RelatoriosFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(label='Nome')
    orientador = django_filters.ModelChoiceFilter(
        queryset=User.objects.filter(groups__name=ORIENTADOR_GROUP_NAME),
        label='Orientadores')
    created = django_filters.DateFilter(label='Envio')
