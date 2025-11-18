from django.shortcuts import render
from django.utils import timezone

from cadastro.models import Cliente
from consulta.models import Anamnese


def index_dashboard(request):
    # Calcular contagens dinâmicas para o dashboard
    total_clientes = Cliente.objects.count()
    today = timezone.localdate()
    agendamentos_hoje = Anamnese.objects.filter(data_consulta__date=today).count()

    context = {
        'total_clientes': total_clientes,
        'agendamentos_hoje': agendamentos_hoje,
    }
    return render(request, 'dashboard/index.html', context)

