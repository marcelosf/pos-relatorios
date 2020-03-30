from django.db import models
from sispos.accounts.models import User


class Relatorios(models.Model):
    nome = models.CharField('Nome', max_length=128)
    relator = models.CharField('Relator', max_length=128, blank=True)
    orientador = models.CharField('Orientador', max_length=128)
    programa = models.CharField('Programa', max_length=20)
    relatorio = models.FileField('Relatório', upload_to='relatorios/%Y/%m/%d/')
    encaminhamento = models.FileField('Encaminhamento', upload_to='encaminhamentos/%Y/%m/%d/')
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
