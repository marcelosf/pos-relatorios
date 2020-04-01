from django.urls import path
from sispos.relatorios.views import relatorios_novo, relatorios_list

app_name = 'relatorios'

urlpatterns = [
    path('novo', relatorios_novo, name='relatorios_new'),
    path('', relatorios_list, name='relatorios_list'),
]
