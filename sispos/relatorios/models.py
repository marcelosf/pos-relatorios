from django.db import models
from django.shortcuts import resolve_url as r
from sispos.accounts.models import User
from uuid import uuid4

SEMESTER_1 = 'Primeiro semestre'
SEMESTER_2 = 'Segundo semestre'
SEMESTER_3 = 'Terceriro semestre'
SEMESTER_4 = 'Quarto semestre'
SEMESTER_5 = 'Quinto semestre'
SEMESTER_6 = 'Sexto semestre'
SEMESTER_7 = 'Sétimo semestre'


SEMESTER_CHOICES = (
    ('rds1', SEMESTER_1),
    ('rds2', SEMESTER_2),
    ('rds3', SEMESTER_3),
    ('rds4', SEMESTER_4),
    ('rds5', SEMESTER_5),
    ('rds6', SEMESTER_6),
    ('rds7', SEMESTER_7),
)

WAITING = 'Aguardando parecer'
DONE = 'Avaliado'

STATUS_CHOICES = (
    ('waiting', WAITING),
    ('done', DONE)
)


def limit_to_relator():
    return {'groups__name': 'relatores'}


class Relatorios(models.Model):
    nome = models.CharField('Nome', max_length=128)
    relator = models.ForeignKey(to=User, related_name='relator',
                                on_delete=models.SET_NULL, null=True,
                                limit_choices_to=limit_to_relator)
    orientador = models.CharField('Orientador', max_length=128)
    programa = models.CharField('Programa', max_length=20)
    relatorio = models.FileField('Relatório', upload_to='relatorios/%Y/%m/%d/')
    encaminhamento = models.FileField('Encaminhamento',
                                      upload_to='encaminhamentos/%Y/%m/%d/')
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    created = models.DateField('envio', auto_now_add=True)
    semestre = models.CharField('semestre', max_length=20,
                                choices=SEMESTER_CHOICES)
    uuid = models.UUIDField('uuid', default=uuid4, editable=False)
    state = models.CharField('state', max_length=20, default=WAITING,
                             choices=STATUS_CHOICES)

    def get_absolute_url(self):
        return r('relatorios:relatorios_update', slug=str(self.uuid))

    def get_parecer_url(self):
        path_name = 'parecer:parecer_{}_new'.format(self.semestre)
        return r(path_name, slug=str(self.uuid))
