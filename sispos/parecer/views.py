from django.shortcuts import render
from sispos.parecer.forms import Rds1Form


def parecer_new(request):
    context = {'form': Rds1Form()}
    return render(request, 'parecer_ds1_new.html', context)
