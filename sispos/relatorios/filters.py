import django_filters
from django.contrib.auth.models import Group
from sispos.relatorios.models import Relatorios


def get_orientadores():
    group_data = {'name': 'orientador'}
    orientadores_group, created = Group.objects.get_or_create(**group_data)
    orientadores = orientadores_group.user_set.all()
    return orientadores


class RelatoriosFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(label='Nome')
    orientador = django_filters.ModelChoiceFilter(queryset=get_orientadores(),
                                                  label='Orientadores')
    created = django_filters.DateFilter(label='Envio')

    class Meta:
        model = Relatorios
        fields = ['nome', 'orientador', 'created']
