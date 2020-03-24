from django import forms


class Relatorios(forms.Form):
    nome = forms.CharField(label='Nome', max_length=256)
    relator = forms.ChoiceField(label='Relator')
    orientador = forms.ChoiceField(label='Orientador')
    programa = forms.ChoiceField(label='Programa')
    relatorio = forms.FileField(label='Relatório')
    encaminhamento = forms.FileField(label='Encaminhamento')
