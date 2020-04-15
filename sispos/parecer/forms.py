from django import forms
from sispos.parecer.models import STATUS_CHOICES


class Rds1Form(forms.Form):
    desempenho = forms.CharField(label='Desempenho nas disciplinas',
                                 max_length=2048, widget=forms.Textarea)
    revisao = forms.CharField(label='Revisão Bibliográfica',
                              max_length=2048, widget=forms.Textarea)
    definicao = forms.CharField(label='Definição do problema',
                                max_length=2048, widget=forms.Textarea)
    plano = forms.CharField(label='Plano de trabalho detalhado',
                            max_length=2048, widget=forms.Textarea)
    resultados = forms.CharField(label='Resultados iniciais',
                                 max_length=2048, widget=forms.Textarea)
    atividades = forms.CharField(label='Outras atividades',
                                 max_length=2048, widget=forms.Textarea)
    status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES)


class Rds2Form(forms.Form):
    desempenho = forms.CharField(label='Desempenho nas disciplinas',
                                 max_length=2048, widget=forms.Textarea)
    metodologia = forms.CharField(label='Metodologia de trabalho',
                                  max_length=2048, widget=forms.Textarea)
    resultados = forms.CharField(label='Resultados',
                                 max_length=2048, widget=forms.Textarea)
    esboco = forms.CharField(label='Esboço de artigo científico',
                             max_length=2048, widget=forms.Textarea)
    atividades = forms.CharField(label='Outras atividades',
                                 max_length=2048, widget=forms.Textarea)
    status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES)


class Rds3Form(forms.Form):
    resultados = forms.CharField(label='Resultados', max_length=2048,
                                 widget=forms.Textarea)
    artigo = forms.CharField(label='Versão final de artigo científico',
                             max_length=2048, widget=forms.Textarea)
    atividades = forms.CharField(label='Outras atividades', max_length=2048,
                                 widget=forms.Textarea)
    status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES)
