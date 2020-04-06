import django_tables2 as tables
from django.shortcuts import resolve_url as r
from django.utils.html import format_html
from sispos.relatorios.models import Relatorios


class RelatoriosTable(tables.Table):
    uuid = tables.Column(verbose_name='Ação')

    def render_uuid(self, value):
        url = r('relatorios:relatorios_update', slug=value)
        tag = '<a class="btn btn-sm btn-outline-primary" \
               href="{}">Detalhar</a>'.format(url)
        return format_html(tag)

    class Meta:
        model = Relatorios
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('nome', 'created', 'orientador', 'uuid')
