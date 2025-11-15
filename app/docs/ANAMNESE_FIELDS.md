# Campos do Modelo Anamnese

Este arquivo lista os campos do modelo `Anamnese` (arquivo: `consulta/models.py`) com descrições curtas.

Campos Principais

- `cliente` (Chave Estrangeira -> Cliente): cliente vinculado à anamnese.
- `data_consulta` (Data e Hora): data e hora da consulta (preenchimento automático).
- `queixa_principal` (Texto Longo): descrição livre da queixa.
- `afeta_outras_partes` (Texto Curto S/N): se a condição afeta outras partes do corpo.
- `afeta_quais_partes` (Texto Longo): quais partes, texto livre.
- `tempo_problema` (Texto Curto): há quanto tempo o problema existe.
- `estado_problema` (Texto Curto com escolhas): Estável / Aumentando / Diminuindo.

Sinais/Alterações no Couro Cabeludo (Campos Sim/Não)
- `dor`, `coceira`, `ardor`, `crostas`, `odor`, `inflamacao`, `feridas`, `caspa`, `oleosidade`, `descamacao`.

Histórico Médico
- `outras_crises` (S/N), `data_outras_crises` (quando), `historico_doencas` (texto),
- `enfermidade_atual` (S/N), `enfermidades` (texto)

Condições Específicas
- `problema_endocrino` (S/N), `quais_endocrinos` (texto)
- `cardiaco` (S/N), `marcapasso` (S/N)

Medicamentos e Cuidados
- `medicamentos` (S/N), `quais_medicamentos` (texto)
- `frequencia_lavagem` (Texto Curto), `produtos_uso` (Texto Longo)

Fatores Recentes
- `fez_dieta`, `emagreceu`, `engordou`, `crise_emocional`, `amamentou` (Campos Sim/Não)

Alergias
- `alergia` (S/N), `quais_alergias` (texto)

Dados Reprodutivos
- `tem_filhos` (S/N), `quantidade_filhos` (número), `data_ultima_gravidez` (data),
- `gravidez_piorou` (S/N), `alteracao_menstruacao` (S/N), `qual_alteracao` (texto)

Dieta e Histórico Familiar
- `come_carne` (S/N), `familiar_mesmo_problema` (S/N), `familiar_calvicie` (S/N)

Cuidados Capilares
- `procedimento_quimico` (S/N), `quais_procedimentos` (texto), `frequencia_procedimentos` (texto)
- `usa_gel`, `usa_bone`, `usa_chapeu`, `usa_penteados`, `usa_escovas`, `usa_capacetes`, `usa_chapas` (Campos Sim/Não)

Exame Físico
- `volume_uniforme` (S/N), `comprimento_uniforme` (S/N), `textura_cabelos` (escolha),
- `estado_pontas` (escolha), `regiao_danificada` (texto)

Condições do Couro Cabeludo e dos Fios
- `couro_oleosidade`, `couro_descamacao`, `couro_prurido`, `couro_vermelhidao`, `couro_manchas`, `couro_caspa`, `couro_odor`, `couro_outros`.
- `fios_nodulos`, `fios_triconodose`, `fios_tricorrexinodosa`, `fios_tricoptilose`, `fios_outros`.

Alopecia e Alterações Locais
- `tem_falhas`, `tem_entradas`, `tem_retracoes` (Campos Sim/Não)
- `regiao_afetada` (texto), campos específicos de alopecia: `alopecia_regiao`, `alopecia_num_lesoes`, `alopecia_formato`, `alopecia_tamanho`, `alopecia_superficie`.

Reposição e Observações
- `reposicao_fios` (S/N), `observacoes` (texto), `alteracao_encontrada` (texto)

Observação: Para mais detalhes e informações de uso, consulte o arquivo `consulta/models.py`.
