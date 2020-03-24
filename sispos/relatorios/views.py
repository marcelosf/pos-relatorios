from django.shortcuts import render


def relatorios_novo(request):
    return render(request, 'relatorios_novo.html')
