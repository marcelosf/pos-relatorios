import django_tables2 as tables
from django.shortcuts import resolve_url as r
from django.utils.html import format_html
from sispos.relatorios.models import Relatorios
from sispos.relatorios import models as states


class RelatoriosTable(tables.Table):
    uuid = tables.Column(verbose_name='Status')
    relator_state = tables.Column(verbose_name='Status', accessor='uuid')

    def render_uuid(self, value):
        return self.make_action_button(states.RELATOR_ASSIGNED, value)

    def render_relator_state(self, value):
        return self.make_action_button(states.PARECER_RELATOR_SUBMITED, value)

    def before_render(self, request):
        user_groups = request.user.groups.all()

        if user_groups.filter(name='coordenadores').exists():
            self.columns.hide('relator_state')

        if user_groups.filter(name='relatores').exists():
            self.columns.hide('uuid')

    def make_action_button(self, success, slug):
        obj = self.data.data.get(uuid=slug)
        html_class = 'btn-outline-success'
        button_name = obj.state
        url = r('relatorios:relatorios_update', slug=slug)
        if not (obj.state == success):
            html_class = 'btn-outline-warning'
            button_name = 'Avaliar'
        tag = '<a class="btn btn-sm btn-block {}" href="{}">{}</a>'
        return format_html(tag, html_class, url, button_name)

    class Meta:
        model = Relatorios
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('nome', 'created', 'relator', 'orientador',
                  'uuid', 'relator_state')
