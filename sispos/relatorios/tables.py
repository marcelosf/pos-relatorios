import django_tables2 as tables
from django.utils.html import format_html
from sispos.relatorios.models import Relatorios


class RelatoriosTable(tables.Table):
    uuid = tables.Column(verbose_name='Ação')

    def render_uuid(self, value):
        tag = '<a class="btn btn-sm btn-outline-primary" \
               href="detalhar/{}">Detalhar</a>'.format(str(value))
        return format_html(tag)

    class Meta:
        model = Relatorios
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('nome', 'created', 'orientador', 'uuid')
