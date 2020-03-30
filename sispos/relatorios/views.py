from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.core import mail
from sispos.relatorios.forms import Relatorios as RelatoriosForm
from sispos.relatorios.models import Relatorios


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
        Relatorios.objects.create(**form.cleaned_data)
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


def send_email_coodenador(to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(settings.EMAIL_SUBJECT, body, settings.EMAIL_FROM, to)
