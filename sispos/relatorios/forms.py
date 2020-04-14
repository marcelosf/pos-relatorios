from django import forms
from django.contrib.auth.models import Group
from sispos.accounts.models import User
from sispos.relatorios.models import SEMESTER_CHOICES


ORIENTADOR_CHOICES = (('Orientador 1', 'Orientador 1'), ('Orientador 2', 'Orientador 2'))
RELATOR_CHOICES = (('Relator 1', 'Relator 1'), ('Relator 2', 'Relator 2'))
PROGRAMA_CHOICES = (('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'))
RELATOR_GROUP_NAME = 'relatores'


class RelatoriosForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=256)
    programa = forms.ChoiceField(label='Programa', choices=PROGRAMA_CHOICES)
    relatorio = forms.FileField(label='Relatório')
    encaminhamento = forms.FileField(label='Encaminhamento')
    semestre = forms.ChoiceField(label='Semestre', choices=SEMESTER_CHOICES)

    def __init__(self, *args, **kwargs):
        super(RelatoriosForm, self).__init__(*args, **kwargs)
        orientadores_group, created = Group.objects.get_or_create(**{'name': 'orientadores'})
        orientadores = orientadores_group.user_set.all()
        self.fields['orientador'] = forms.ModelChoiceField(queryset=orientadores, label='Orientadores')


class CoordenadorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CoordenadorForm, self).__init__()
        Group.objects.get_or_create(**{'name': RELATOR_GROUP_NAME})
        coordenadores = User.objects.filter(groups__name=RELATOR_GROUP_NAME)
        self.fields['relator'] = forms.ModelChoiceField(queryset=coordenadores,
                                                        label='Coordenador')
