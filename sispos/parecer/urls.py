from django.urls import path
from sispos.parecer import views

app_name = 'parecer'

urlpatterns = [
    path('<slug:slug>/rds1/novo', views.parecer_rds1_new, name='parecer_rds1_new'),
    path('<slug:slug>/rds2/novo', views.parecer_rds2_new, name='parecer_rds2_new'),
    path('<slug:slug>/rds3/novo', views.parecer_rds3_new, name='parecer_rds3_new'),
    path('<slug:slug>/rds4/novo', views.parecer_rds4_new, name='parecer_rds4_new'),
]
