from django.shortcuts import render
from django.views.generic import CreateView
from sispos.parecer.forms import Rds1Form
from sispos.parecer.models import Rds1


class Rds1Create(CreateView):
    fields = ['desempenho', 'revisao', 'definicao',
              'plano', 'resultados', 'atividades']
    model = Rds1
    template_name = 'parecer_ds1_new.html'
    slug_field = 'uuid'


parecer_new = Rds1Create.as_view()

"""
def parecer_new(request):
    context = {'form': Rds1Form()}
    return render(request, 'parecer_ds1_new.html', context)
"""