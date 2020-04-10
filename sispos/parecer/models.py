from django.db import models
from sispos.relatorios.models import Relatorios
from sispos.accounts.models import User


class Rds1(models.Model):
    desempenho = models.CharField('desempenho', max_length=2048)
    revisao = models.CharField('revisao', max_length=2048)
    definicao = models.CharField('definicao', max_length=2048)
    plano = models.CharField('planos', max_length=2048)
    resultados = models.CharField('resultados', max_length=2048)
    atividades = models.CharField('atividades', max_length=2048)
    relatorio = models.ForeignKey(Relatorios, on_delete=models.CASCADE)
    relator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
