from django import forms
from .models import Cliente
from django.core.exceptions import ValidationError
import re

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf', 'data_nascimento', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome completo do cliente',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@exemplo.com',
                'class': 'form-control',
            }),
            'telefone': forms.TextInput(attrs={
                'placeholder': '(00) 00000-0000',
                'class': 'form-control',
            }),
            'cpf': forms.TextInput(attrs={
                'placeholder': '000.000.000-00',
                'class': 'form-control',
            }),
            'data_nascimento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'endereco': forms.TextInput(attrs={
                'placeholder': 'Rua, número, bairro, cidade - UF',
                'class': 'form-control',
            }),
        }
        help_texts = {
            'cpf': 'Digite apenas números. A formatação será aplicada automaticamente.',
            'telefone': 'Digite apenas números com DDD. Ex: 11999999999',
            'data_nascimento': 'Selecione a data de nascimento no calendário.',
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            # Remove caracteres não numéricos
            cpf = re.sub(r'[^0-9]', '', cpf)
            if len(cpf) != 11:
                raise ValidationError('CPF deve ter 11 dígitos.')
            # Formata o CPF
            cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        return cpf

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone:
            # Remove caracteres não numéricos
            telefone = re.sub(r'[^0-9]', '', telefone)
            if len(telefone) < 10 or len(telefone) > 11:
                raise ValidationError('Telefone deve ter 10 ou 11 dígitos.')
            # Formata o telefone
            if len(telefone) == 11:
                telefone = f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}'
            else:
                telefone = f'({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}'
        return telefone