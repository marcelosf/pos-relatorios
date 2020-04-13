from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import resolve_url as r
from sispos.parecer.forms import Rds1Form, Rds2Form
from sispos.relatorios.models import Relatorios
from sispos.parecer.models import Rds1


def parecer_new(request, slug):
    if request.method == 'POST':
        create_rds1(request, slug)
    context = {'form': Rds1Form(), 'slug': slug}
    return render(request, 'parecer_ds1_new.html', context)


def parecer_rds2_new(request, slug):
    context = {'slug': slug, 'form': Rds2Form(),
               'action': r('parecer:parecer_rds2_new', slug=slug)}
    return render(request, 'parecer_new.html', context)


def create_rds1(request, slug):
    form = Rds1Form(request.POST)
    if form.is_valid():
        relatorio = Relatorios.objects.get(uuid=slug)
        form.cleaned_data['relatorio'] = relatorio
        form.cleaned_data['relator'] = request.user
        Rds1.objects.create(**form.cleaned_data)
        context = {'form': form, 'slug': slug}
        messages.success(request, 'Parecer enviado com sucesso.')
        return render(request, 'parecer_ds1_new.html', context)
    messages.error(request, 'Não foi possível enviar o parecer.')
    context = {'form': form, 'slug': slug}
    return render(request, 'parecer_ds1_new.html', context)
