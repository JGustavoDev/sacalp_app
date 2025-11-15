from django.urls import path
from . import views

app_name = 'cadastro'

urlpatterns = [
    path('novo/', views.cadastra_cliente, name='cadastra_cliente'),
    path('lista/', views.listar_clientes, name='listar_clientes'),
    path('cliente/<int:pk>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('cliente/<int:pk>/editar/', views.EditarCliente.as_view(), name='editar_cliente'),
    path('cliente/<int:pk>/excluir/', views.ExcluirCliente.as_view(), name='excluir_cliente'),
]