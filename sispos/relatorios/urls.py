from django.urls import path
from sispos.relatorios.views import relatorios_novo

app_name = 'relatorios'

urlpatterns = [
    path('novo', relatorios_novo, name='relatorios_new'),
]
