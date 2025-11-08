# CHANGELOG

Registro das mudanças significativas feitas durante a sessão de desenvolvimento.

## 2025-11-07 — Implementação inicial e refinamentos

- Criado app `consulta` com modelo `Anamnese` (muitos campos cobrindo questionário capilar).
- Criado `AnamneseForm` em `consulta/forms.py` com classes Bootstrap aplicadas.
- Criado templates em `consulta/templates/consulta/`:
  - `form.html` — formulário de anamnese (cards, campos agrupados, JS para campos dependentes)
  - `list.html` — listagem de anamneses
  - `detail.html` — visualização detalhada de anamnese
- Criadas views em `consulta/views.py`: `listar_anamneses`, `nova_anamnese`, `detalhe_anamnese`, `editar_anamnese`.
- Adicionado redirecionamento em `cadastro/views.py` para iniciar nova anamnese após criar cliente.
- Registrado app `consulta` em `projeto/settings.py` e adicionado rota em `projeto/urls.py`.
- Executadas migrações: `makemigrations` e `migrate` para `cadastro` e `consulta`.
- Corrigido problema de template (removido filtro inexistente `split` e passado `scalp_fields` pelo view).
- Atualizado `consulta/form.html` para incluir todo o questionário e script JS para toggles.

## Notas

- Várias pequenas correções feitas durante a iteração (templates, views e settings) para garantir que o projeto rode localmente.
