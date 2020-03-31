from django import forms
from django.contrib.auth.models import Group


ORIENTADOR_CHOICES = (('Orientador 1', 'Orientador 1'), ('Orientador 2', 'Orientador 2'))
RELATOR_CHOICES = (('Relator 1', 'Relator 1'), ('Relator 2', 'Relator 2'))
PROGRAMA_CHOICES = (('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'))


class RelatoriosForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=256)
    programa = forms.ChoiceField(label='Programa', choices=PROGRAMA_CHOICES)
    relatorio = forms.FileField(label='Relatório')
    encaminhamento = forms.FileField(label='Encaminhamento')

    def __init__(self, *args, **kwargs):
        super(RelatoriosForm, self).__init__(*args, **kwargs)
        orientadores_group, created = Group.objects.get_or_create(**{'name': 'orientadores'})
        orientadores = orientadores_group.user_set.all()
        choices = [(user.id, user.get_full_name()) for user in orientadores]
        self.fields['orientador'] = forms.ChoiceField(label='Orientador',choices=choices)
