from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django_tables2 import SingleTableView, LazyPaginator
from sispos.relatorios.forms import RelatoriosForm
from sispos.relatorios.tables import RelatoriosTable
from sispos.relatorios.models import Relatorios


class RelatoriosList(SingleTableView):
    model = Relatorios
    table_class = RelatoriosTable
    template_name = 'relatorios_list.html'
    paginator_class = LazyPaginator


relatorios_list = RelatoriosList.as_view()


@login_required(login_url=settings.LOGIN_URL)
def relatorios_novo(request):
    if not request.method == 'POST':
        form = RelatoriosForm(initial={'nome': request.user.get_full_name()})
        return render(request, 'relatorios_novo.html', {'form': form})
    form = create_relatorio(request)
    return render(request, 'relatorios_novo.html', {'form': form})


def create_relatorio(request):
    form = RelatoriosForm(request.POST, request.FILES)
    if form.is_valid():
        request.user.relatorios_set.create(**form.cleaned_data)
        messages.success(request, 'Relatório enviado com sucesso.')
        _send_email(
            user=request.user,
            template_name='email_aluno.txt',
            context={'subscription': form.cleaned_data}
        )
    return form


def _send_email(user, template_name, context):
    body = render_to_string(template_name, context)
    user.email_user(settings.EMAIL_SUBJECT, body, settings.EMAIL_FROM)
