from django.db import models
from django.urls import reverse

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    endereco = models.CharField('Endereço', max_length=200)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('cadastro:detalhe_cliente', args=[self.pk])