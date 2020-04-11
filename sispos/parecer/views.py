from django.shortcuts import render
from sispos.parecer.forms import Rds1Form
from sispos.relatorios.models import Relatorios
from sispos.parecer.models import Rds1


def parecer_new(request, slug):
    if request.method == 'POST':
        create_rds1(request, slug)
    context = {'form': Rds1Form()}
    return render(request, 'parecer_ds1_new.html', context)


def create_rds1(request, slug):
    form = Rds1Form(request.POST)
    if form.is_valid():
        relatorio = Relatorios.objects.get(uuid=slug)
        form.cleaned_data['relatorio'] = relatorio
        form.cleaned_data['relator'] = request.user
        Rds1.objects.create(**form.cleaned_data)
