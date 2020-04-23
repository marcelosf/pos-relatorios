import django_tables2 as tables
from django.shortcuts import resolve_url as r
from django.utils.html import format_html
from sispos.relatorios.models import Relatorios


class RelatoriosTable(tables.Table):
    uuid = tables.Column(verbose_name='Status')

    def render_uuid(self, value):
        if self.user.has_perm('relatorios.change_relatorios'):
            return self.make_action_button('relator_asigned', value)

        if self.user.has_perm('relatorios.add_rds1'):
            return self.make_action_button('parecer_relator_submited', value)

        self.columns.hide('uuid')

    def before_render(self, request):
        self.user = request.user

    def make_action_button(self, success, slug):
        obj = self.data.data.get(uuid=slug)
        html_class = 'btn-outline-success'
        button_name = obj.get_state_display()
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
                  'uuid',)
