from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import resolve_url as r
from sispos.parecer.forms import Rds1Form, Rds2Form, Rds3Form, Rds4Form
from sispos.relatorios.models import Relatorios
from sispos.parecer.models import Rds1, Rds2, Rds3, Rds4


def parecer_new(request, slug):
    if request.method == 'POST':
        create_parecer(request, slug, Rds1, Rds1Form)
    context = {'form': Rds1Form(), 'slug': slug,
               'action': r('parecer:parecer_new', slug=slug)}
    return render(request, 'parecer_new.html', context)


def parecer_rds2_new(request, slug):
    if request.method == 'POST':
        create_parecer(request, slug, Rds2, Rds2Form)
    context = {'slug': slug, 'form': Rds2Form(),
               'action': r('parecer:parecer_rds2_new', slug=slug)}
    return render(request, 'parecer_new.html', context)


def parecer_rds3_new(request, slug):
    if request.method == 'POST':
        create_parecer(request, slug, Rds3, Rds3Form)
    context = {'form': Rds3Form(), 'slug': slug,
               'action': r('parecer:parecer_rds3_new', slug=slug)}
    return render(request, 'parecer_new.html', context)


def parecer_rds4_new(request, slug):
    if request.method == 'POST':
        create_parecer(request, slug, Rds4, Rds4Form)
    context = {'form': Rds4Form(), 'slug': slug,
               'action': r('parecer:parecer_rds4_new', slug=slug)}
    return render(request, 'parecer_new.html', context)


def create_parecer(request, slug, model, form_class):
    form = form_class(request.POST)
    context = {'form': form, 'slug': slug,
               'action': r('parecer:parecer_new.html', slug=slug)}
    if form.is_valid():
        relatorio = Relatorios.objects.get(uuid=slug)
        form.cleaned_data['relatorio'] = relatorio
        form.cleaned_data['relator'] = request.user
        model.objects.create(**form.cleaned_data)
        messages.success(request, 'Parecer enviado com sucesso.')
        return render(request, 'parecer_new.html', context)
    messages.error(request, 'Não foi possível enviar o parecer.')
    return render(request, 'parecer_new.html', context)
