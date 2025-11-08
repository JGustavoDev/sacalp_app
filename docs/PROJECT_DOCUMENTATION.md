# Documentação do Projeto — Visão Geral

Resumo rápido

Este projeto Django (localizado em `c:\Users\guhfe\OneDrive\Desktop\app`) é uma aplicação para cadastro de clientes e registro de consultas/anamneses capilares. Os apps principais são:

- `dashboard` — templates e páginas gerais (base do layout).
- `cadastro` — cadastro de clientes (modelo `Cliente`, views, formulários, templates).
- `consulta` — gestão de anamneses (modelo `Anamnese`, formulário complexo, views de CRUD, templates).

Arquitetura e arquivos importantes

- `projeto/` — pasta do Django project (contém `settings.py`, `urls.py`, `wsgi.py`, etc.).
  - `projeto/settings.py` — registrou os apps `dashboard`, `cadastro`, `consulta` e `widget_tweaks`.
  - `projeto/urls.py` — inclui rotas para `dashboard`, `cadastro` e `consulta`.

- `cadastro/`
  - `models.py` — define o modelo `Cliente`.
  - `forms.py` — `ClienteForm` (formulário de cadastro).
  - `views.py` — funções para criar, listar, detalhar, editar e excluir clientes.
  - `templates/cadastro/` — templates relacionados.

- `consulta/`
  - `models.py` — define o modelo `Anamnese` com muitos campos cobrindo o questionário clinico.
  - `forms.py` — `AnamneseForm`, aplica classes Bootstrap nos widgets e pequenas customizações.
  - `views.py` — `listar_anamneses`, `nova_anamnese`, `detalhe_anamnese`, `editar_anamnese`.
  - `urls.py` — rotas do app (listar, nova/<cliente_id>, detalhe/<pk>, editar/<pk>).
  - `templates/consulta/` — `form.html`, `list.html`, `detail.html` (formulário extenso e páginas para listar e ver detalhes).

O que foi implementado (alto nível)

- Modelos e migrações:
  - `cadastro` e `consulta` migrados (executadas `makemigrations` e `migrate`).
- Formulário de anamnese:
  - `form.html` implementa o questionário completo, dividido em cards, com JS para mostrar/ocultar campos dependentes.
- Fluxo de trabalho:
  - Ao cadastrar um cliente (via `cadastro.cadastra_cliente`) o usuário é redirecionado automaticamente para `consulta:nova_anamnese` daquele cliente.
- Templates:
  - `consulta/form.html` (formulário completo com campos agrupados), `consulta/list.html`, `consulta/detail.html`.

Decisões e notas

- O formulário usa `widget_tweaks` para facilitar classes Bootstrap. O `AnamneseForm` adiciona classes `form-control`/`form-check-input`/`form-select` conforme o tipo do campo.
- Para evitar uso de filtros inexistentes no template, a lista de campos do couro cabeludo é fornecida pelo view via `scalp_fields`.

Próximos passos recomendados

- Refatorar o template para campos explicitamente renderizados (evita iterar sobre todo o form).
- Adicionar testes automatizados que cubram criação de Cliente e Anamnese (unit tests e/ou integração).
- Melhorar UX: dividir o formulário em etapas/abas, salvar rascunho, validação mais detalhada no servidor.
