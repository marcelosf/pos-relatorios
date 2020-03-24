from django.shortcuts import render
from sispos.relatorios.forms import Relatorios


def relatorios_novo(request):
    form = Relatorios()
    return render(request, 'relatorios_novo.html', {'form': form})
