from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Anamnese
from .forms import AnamneseForm
from cadastro.models import Cliente

def listar_anamneses(request):
    anamneses = Anamnese.objects.select_related('cliente').all()
    return render(request, 'consulta/list.html', {'anamneses': anamneses})

def nova_anamnese(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    scalp_fields = ['dor','coceira','ardor','crostas','odor','inflamacao','feridas','caspa','oleosidade','descamacao']

    if request.method == 'POST':
        form = AnamneseForm(request.POST)
        if form.is_valid():
            anamnese = form.save(commit=False)
            anamnese.cliente = cliente
            anamnese.save()
            messages.success(request, 'Anamnese cadastrada com sucesso!')
            return redirect('consulta:detalhe_anamnese', pk=anamnese.pk)
    else:
        form = AnamneseForm()

    return render(request, 'consulta/form.html', {
        'form': form,
        'cliente': cliente,
        'titulo': 'Nova Consulta',
        'scalp_fields': scalp_fields,
    })

def detalhe_anamnese(request, pk):
    anamnese = get_object_or_404(Anamnese.objects.select_related('cliente'), pk=pk)
    return render(request, 'consulta/detail.html', {'anamnese': anamnese})

def editar_anamnese(request, pk):
    anamnese = get_object_or_404(Anamnese.objects.select_related('cliente'), pk=pk)
    scalp_fields = ['dor','coceira','ardor','crostas','odor','inflamacao','feridas','caspa','oleosidade','descamacao']

    if request.method == 'POST':
        form = AnamneseForm(request.POST, instance=anamnese)
        if form.is_valid():
            form.save()
            messages.success(request, 'Anamnese atualizada com sucesso!')
            return redirect('consulta:detalhe_anamnese', pk=anamnese.pk)
    else:
        form = AnamneseForm(instance=anamnese)

    return render(request, 'consulta/form.html', {
        'form': form,
        'cliente': anamnese.cliente,
        'titulo': 'Editar Consulta',
        'scalp_fields': scalp_fields,
    })