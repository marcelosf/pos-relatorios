from django import forms


RELATOR_CHOICES = (('Relator 1', 'Relator 1'), ('Relator 2', 'Relator 2'))
ORIENTADOR_CHOICES = (('Orientador 1', 'Orientador 1'), ('Orientador 2', 'Orientador 2'))
PROGRAMA_CHOICES = (('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'))


class Relatorios(forms.Form):
    nome = forms.CharField(label='Nome', max_length=256)
    relator = forms.ChoiceField(label='Relator', choices=RELATOR_CHOICES, required=False)
    orientador = forms.ChoiceField(label='Orientador', choices=ORIENTADOR_CHOICES)
    programa = forms.ChoiceField(label='Programa', choices=PROGRAMA_CHOICES)
    relatorio = forms.FileField(label='Relatório')
    encaminhamento = forms.FileField(label='Encaminhamento')
