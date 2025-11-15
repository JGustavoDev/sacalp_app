from django.urls import path
from . import views

app_name = 'consulta'

urlpatterns = [
    path('', views.listar_anamneses, name='listar_anamneses'),
    path('nova/<int:cliente_id>/', views.nova_anamnese, name='nova_anamnese'),
    path('<int:pk>/', views.detalhe_anamnese, name='detalhe_anamnese'),
    path('<int:pk>/editar/', views.editar_anamnese, name='editar_anamnese'),
]
