from django import forms


class Rds1Form(forms.Form):
    desempenho = forms.CharField()
    revisao = forms.CharField()
    definicao = forms.CharField()
    plano = forms.CharField()
    resultados = forms.CharField()
    atividades = forms.CharField()
    relatorio = forms.HiddenInput()
