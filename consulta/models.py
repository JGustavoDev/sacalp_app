from django.db import models
from cadastro.models import Cliente


class Anamnese(models.Model):
	OPCOES_SIM_NAO = [
		("S", "Sim"),
		("N", "Não"),
	]

	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="anamneses")
	data_consulta = models.DateTimeField(auto_now_add=True)

	# Queixa principal
	queixa_principal = models.TextField("Queixa principal")
	afeta_outras_partes = models.CharField("Afeta outras partes do corpo?", max_length=1, choices=OPCOES_SIM_NAO)
	afeta_quais_partes = models.TextField("Quais partes afeta?", blank=True)
	tempo_problema = models.CharField("Há quanto tempo?", max_length=100, blank=True)

	OPCOES_ESTADO = [
		("E", "Estável"),
		("A", "Aumentando"),
		("D", "Diminuindo"),
	]
	estado_problema = models.CharField("Estado do problema", max_length=1, choices=OPCOES_ESTADO, blank=True)

	# Couro cabeludo / sinais
	cabelo_mais_quebradiço = models.BooleanField("Cabelo mais quebradiço", default=False)
	dor = models.BooleanField("Dor", default=False)
	coceira = models.BooleanField("Coceira", default=False)
	ardor = models.BooleanField("Ardor", default=False)
	crostas = models.BooleanField("Crostas", default=False)
	odor = models.BooleanField("Odor", default=False)
	inflamacao = models.BooleanField("Inflamação", default=False)
	feridas = models.BooleanField("Feridas", default=False)
	caspa = models.BooleanField("Caspa", default=False)
	oleosidade = models.BooleanField("Oleosidade", default=False)
	descamacao = models.BooleanField("Descamação", default=False)

	# Histórico médico
	outras_crises = models.CharField("Já teve outras crises?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	data_outras_crises = models.CharField("Quando teve outras crises?", max_length=100, blank=True)
	historico_doencas = models.TextField("Histórico de doenças recentes", blank=True)
	enfermidade_atual = models.CharField("Alguma enfermidade atual?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	enfermidades = models.TextField("Quais enfermidades?", blank=True)

	problema_endocrino = models.CharField("Problema endócrino?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	quais_endocrinos = models.TextField("Quais problemas endócrinos?", blank=True)
	cardiaco = models.CharField("É cardíaco?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	marcapasso = models.CharField("Usa marcapasso?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)

	medicamentos = models.CharField("Toma medicamentos?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	quais_medicamentos = models.TextField("Quais medicamentos?", blank=True)

	frequencia_lavagem = models.CharField("Frequência de lavagem do cabelo", max_length=100, blank=True)
	produtos_uso = models.TextField("Produtos capilares em uso", blank=True)

	fez_dieta = models.BooleanField("Fez dieta", default=False)
	emagreceu = models.BooleanField("Emagreceu", default=False)
	engordou = models.BooleanField("Engordou", default=False)
	crise_emocional = models.BooleanField("Teve crise emocional", default=False)
	amamentou = models.BooleanField("Amamentou", default=False)

	alergia = models.CharField("Tem alergia?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	quais_alergias = models.TextField("Quais alergias?", blank=True)

	tem_filhos = models.CharField("Tem filhos?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	quantidade_filhos = models.IntegerField("Quantidade de filhos", null=True, blank=True)
	data_ultima_gravidez = models.DateField("Data da última gravidez", null=True, blank=True)
	gravidez_piorou = models.CharField("Gravidez piorou o problema?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	alteracao_menstruacao = models.CharField("Alteração na menstruação?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	qual_alteracao = models.TextField("Qual alteração?", blank=True)

	come_carne = models.CharField("Come carne?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	familiar_mesmo_problema = models.CharField("Familiar com mesmo problema?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	familiar_calvicie = models.CharField("Familiar com calvície?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)

	procedimento_quimico = models.CharField("Faz procedimento químico?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	quais_procedimentos = models.TextField("Quais procedimentos?", blank=True)
	frequencia_procedimentos = models.CharField("Frequência dos procedimentos", max_length=100, blank=True)

	usa_gel = models.BooleanField("Usa gel", default=False)
	usa_bone = models.BooleanField("Usa boné", default=False)
	usa_chapeu = models.BooleanField("Usa chapéu", default=False)
	usa_penteados = models.BooleanField("Usa penteados presos", default=False)
	usa_escovas = models.BooleanField("Usa escovas", default=False)
	usa_capacetes = models.BooleanField("Usa capacetes", default=False)
	usa_chapas = models.BooleanField("Usa chapas", default=False)

	volume_uniforme = models.CharField("Volume uniforme?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	comprimento_uniforme = models.CharField("Comprimento uniforme?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)

	OPCOES_TEXTURA = [
		("A", "Ásperos"),
		("M", "Macios"),
		("B", "Brilhantes"),
		("O", "Opacos"),
	]
	textura_cabelos = models.CharField("Textura dos cabelos", max_length=1, choices=OPCOES_TEXTURA, blank=True)

	OPCOES_PONTAS = [
		("I", "Íntegras"),
		("Q", "Quebradiças"),
	]
	estado_pontas = models.CharField("Estado das pontas", max_length=1, choices=OPCOES_PONTAS, blank=True)
	regiao_danificada = models.TextField("Região mais danificada", blank=True)

	couro_oleosidade = models.BooleanField("Oleosidade no couro", default=False)
	couro_descamacao = models.BooleanField("Descamação no couro", default=False)
	couro_prurido = models.BooleanField("Prurido no couro", default=False)
	couro_vermelhidao = models.BooleanField("Vermelhidão no couro", default=False)
	couro_manchas = models.BooleanField("Manchas no couro", default=False)
	couro_caspa = models.BooleanField("Caspa no couro", default=False)
	couro_odor = models.BooleanField("Odor no couro", default=False)
	couro_outros = models.TextField("Outros problemas no couro", blank=True)

	fios_nodulos = models.BooleanField("Nódulos nos fios", default=False)
	fios_triconodose = models.BooleanField("Triconodose", default=False)
	fios_tricorrexinodosa = models.BooleanField("Tricorrexinodosa", default=False)
	fios_tricoptilose = models.BooleanField("Tricoptilose", default=False)
	fios_outros = models.TextField("Outras condições nos fios", blank=True)

	tem_falhas = models.BooleanField("Presença de falhas", default=False)
	tem_entradas = models.BooleanField("Presença de entradas", default=False)
	tem_retracoes = models.BooleanField("Presença de retrações", default=False)
	regiao_afetada = models.TextField("Região afetada", blank=True)

	alopecia_regiao = models.CharField("Região da alopecia", max_length=100, blank=True)
	alopecia_num_lesoes = models.IntegerField("Número de lesões", null=True, blank=True)
	alopecia_formato = models.CharField("Formato das lesões", max_length=100, blank=True)
	alopecia_tamanho = models.CharField("Tamanho das lesões", max_length=100, blank=True)
	alopecia_superficie = models.TextField("Superfície do couro cabeludo no local", blank=True)

	reposicao_fios = models.CharField("Existe reposição dos fios?", max_length=1, choices=OPCOES_SIM_NAO, blank=True)
	observacoes = models.TextField("Observações complementares", blank=True)
	alteracao_encontrada = models.TextField("Alteração encontrada", blank=True)

	class Meta:
		verbose_name = "Anamnese"
		verbose_name_plural = "Anamneses"
		ordering = ["-data_consulta"]

	def __str__(self):
		return f"Anamnese de {self.cliente.nome} em {self.data_consulta.strftime('%d/%m/%Y')}"
