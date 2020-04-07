from django.db import models
from django.shortcuts import resolve_url as r
from sispos.accounts.models import User
from uuid import uuid4


def limit_to_relator():
    return {'groups__name': 'relatores'}


class Relatorios(models.Model):
    nome = models.CharField('Nome', max_length=128)
    relator = models.ForeignKey(to=User, related_name='relator', on_delete=models.SET_NULL, null=True, limit_choices_to=limit_to_relator)
    orientador = models.CharField('Orientador', max_length=128)
    programa = models.CharField('Programa', max_length=20)
    relatorio = models.FileField('Relatório', upload_to='relatorios/%Y/%m/%d/')
    encaminhamento = models.FileField('Encaminhamento', upload_to='encaminhamentos/%Y/%m/%d/')
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    created = models.DateField('envio', auto_now_add=True)
    uuid = models.UUIDField('uuid', default=uuid4, editable=False)

    def get_absolute_url(self):
        return r('relatorios:relatorios_update', slug=str(self.uuid))
