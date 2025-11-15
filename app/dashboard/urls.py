from django.shortcuts import render
from django.urls import path

from . import views

# Declare the application namespace so templates can use the
# namespaced reversal: {% url 'dashboard:index' %}
app_name = 'dashboard'

urlpatterns = [
    # Rota principal do aplicativo dashboard
    path('', views.index_dashboard, name='index'),
]