from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

def cadastra_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                cliente = form.save()
                messages.success(request, 'Cliente cadastrado com sucesso!')
                # Após criar o cliente, iniciar nova anamnese para este cliente
                return redirect('consulta:nova_anamnese', cliente.pk)
            except Exception as e:
                messages.error(request, 'Erro ao salvar o cliente. Por favor, verifique os dados.')
    else:
        form = ClienteForm()
    
    return render(request, 'cadastro/form.html', {'form': form})

def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('nome')
    context = {
        'clientes': clientes,
        'tem_clientes': Cliente.objects.exists(),
    }
    return render(request, 'cadastro/list.html', context)

def detalhe_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cadastro/detail.html', {'cliente': cliente})

class EditarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('cadastro:listar_clientes')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return super().form_valid(form)

class ExcluirCliente(DeleteView):
    model = Cliente
    template_name = 'cadastro/confirm_delete.html'
    success_url = reverse_lazy('cadastro:listar_clientes')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Cliente excluído com sucesso!')
        return super().delete(request, *args, **kwargs)