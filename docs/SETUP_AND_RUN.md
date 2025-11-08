# Setup e Como Executar o Projeto (Windows / PowerShell)

Pré-requisitos

- Python 3.11+ (você tem Python 3.13 instalado conforme traceback). 
- pip
- (Opcional) Virtualenv / venv

Passos rápidos

1. Abra o PowerShell e vá para a raiz do projeto (onde está `manage.py`):

```powershell
cd c:\Users\guhfe\OneDrive\Desktop\app\projeto
```

2. (Opcional) criar e ativar um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instalar dependências (se houver `requirements.txt`). Se não houver, instale pelo menos Django e widget_tweaks:

```powershell
pip install Django==5.2.7 django-widget-tweaks
```

4. Aplicar migrações (cria as tabelas necessárias):

```powershell
python manage.py makemigrations
python manage.py migrate
```

5. Criar um superusuário (opcional, para acessar o admin):

```powershell
python manage.py createsuperuser
```

6. Rodar o servidor de desenvolvimento:

```powershell
python manage.py runserver
```

7. Acessar no navegador:

- Admin: http://127.0.0.1:8000/admin/
- Página principal do app (dependendo de rota): http://127.0.0.1:8000/
- Listagem de consultas: http://127.0.0.1:8000/consulta/

Observações

- Se você alterar models, rode `makemigrations` e `migrate` novamente.
- O template `consulta/form.html` depende de `widget_tweaks` para classes; certifique-se de ter o pacote instalado.
