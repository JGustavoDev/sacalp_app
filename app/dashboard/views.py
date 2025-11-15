from django.shortcuts import render
from django.shortcuts import render

def index_dashboard(request):
    # Contexto simples para a primeira página
    context = {
        'total_clientes': 150,
        'agendamentos_hoje': 25,
    }
    return render(request, 'dashboard/index.html', context)

