from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
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
    return form
