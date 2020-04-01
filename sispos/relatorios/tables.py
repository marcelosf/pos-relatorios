import django_tables2 as tables
from sispos.relatorios.models import Relatorios


class RelatoriosTable(tables.Table):
    class Meta:
        model = Relatorios
        template_name = 'django_tables2/bootstrap.html'
        fields = ('nome', 'created', 'orientador')
