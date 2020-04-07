from django.urls import path
from sispos.relatorios import views

app_name = 'relatorios'

urlpatterns = [
    path('', views.relatorios_list, name='relatorios_list'),
    path('novo', views.relatorios_novo, name='relatorios_new'),
    path('update/<slug:slug>/', views.relatorios_update, name='relatorios_update')
]
