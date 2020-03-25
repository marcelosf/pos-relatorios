from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from sispos.relatorios.forms import Relatorios


@login_required(login_url=settings.LOGIN_URL)
def relatorios_novo(request):
    form = Relatorios()
    return render(request, 'relatorios_novo.html', {'form': form})
