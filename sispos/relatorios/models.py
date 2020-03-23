from django.db import models


class Relatorios(models.Model):
    nome = models.CharField('Nome', max_length=128)
    relator = models.CharField('Relator', max_length=128)
    orientador = models.CharField('Orientador', max_length=128)
    programa = models.CharField('Programa', max_length=20)
    relatorio = models.CharField('Relatório', max_length=20)
    encaminhamento = models.CharField('Encaminhamento', max_length=20)
