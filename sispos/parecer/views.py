from django.views.generic import CreateView
from sispos.parecer.models import Rds1


class Rds1Create(CreateView):
    fields = ['desempenho', 'revisao', 'definicao',
              'plano', 'resultados', 'atividades']
    model = Rds1
    template_name = 'parecer_ds1_new.html'
    slug_field = 'uuid'


parecer_new = Rds1Create.as_view()
