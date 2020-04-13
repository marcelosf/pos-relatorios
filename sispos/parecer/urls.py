from django.urls import path
from sispos.parecer import views

app_name = 'parecer'

urlpatterns = [
    path('<slug:slug>/novo', views.parecer_new, name='parecer_new'),
]
