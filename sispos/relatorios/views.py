from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from sispos.relatorios.forms import Relatorios as RelatoriosForm
from sispos.relatorios.models import Relatorios


@login_required(login_url=settings.LOGIN_URL)
def relatorios_novo(request):
    form = RelatoriosForm()
    if not request.method == 'POST':
        return render(request, 'relatorios_novo.html', {'form': form})
    form = create_relatorio(request)
    return render(request, 'relatorios_novo.html', {'form': form})


def create_relatorio(request):
    form = RelatoriosForm(request.POST, request.FILES)
    if form.is_valid():
        Relatorios.objects.create(**form.cleaned_data)
        messages.success(request, 'Relatório enviado com sucesso.')
    return form
