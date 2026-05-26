
import sys

# Exercicio 2

# print(sys.version)
# print(sys.platform)

# def soma (a,b):
#     """
#     Função de soma parametros.
#     Args:
#         - a(any): primeiro argumento de função soma. 
#         - B(any): segunudo argumento de função soma. 
#     Return:
#         Um único valor.
#     """
      

#     return a + b
# # Primeiro argumento
# a = int(input("a:"))
# b = int(input("b:"))
# #----------------------------------
# print (soma(a,b))

#====================================

# Exercicio 3
# import this

#====================================

# Exercicio 4

# nome ="Leonam De Sousa"
# idade = 22
# salario = 2350.00
# ativo = True
# print(nome,idade,salario,ativo)

#====================================

# Exercicio 5

# print("Bem-vindo ao curso full-stack")
# nome = "Leonam"
# print("Aluno:" + nome)
# print ("Curso de Python") #Faltou as aspas simples ou duplas

#====================================

# Exercicio 6

# ano_atual = 2026
# temperatura = 36.9
# cidade = "Boa Vista"
# previsao= None
# string_vazia = ""

# print(f"{ano_atual},{type(ano_atual)}")
# print(f"{temperatura},{type(temperatura)}")
# print(f"'{cidade}',{type(cidade)}")
# print(f"{previsao},{type(previsao)}")
# print(f"'{string_vazia}',{type(string_vazia)}")

#====================================

# Exercicio 7

# largura = float(input("LARGURA: " ))
# comprimento = float(input("COMPRIMENTO: " ))

# resultado = largura * comprimento

# print(f"Área do terreno: {resultado} m²")

#====================================

# Exercicio 8 

# C = float(input("Temperatura em Celsius: "))
# F = (C*9/5)*32
# K = C + 273.15

# print(f"""Em Kelvin: {K}°,
# Em Farenheit: {F}º 
# Em Celsius: {C}° """)

#====================================

#Exercicio 9 

# Nome = str(input("Como se chama: "))
# idade_texto= input("Quantos anos tem: ")

# idade = int(idade_texto)

# ano_nascimento = 2026 - idade

# print(f"Olá,{Nome}! Você tem {idade} anos e nasceu por volta de {ano_nascimento}")

#====================================

# Exercicio 10

# capacidade_caminhao = 850
# peso_caixa = 32

#Cálculos utilizando operadores aritméticos de divisão inteira e resto
# caixas_completas = capacidade_caminhao // peso_caixa
# peso_restante = capacidade_caminhao % peso_caixa

# print(f"Quantidade de caixas completas que cabem no caminhão: {caixas_completas} caixas.")
# print(f"Peso restante que não completa uma caixa extra: {peso_restante} kg.")
    
#====================================
  
# Exercicio 11
    
# nome = "Mariana Souza"
# cargo = "Analista de Dados"
# salario = 7850.50
# anos_empresa = 3

# print("=============================")
# print(f"     FICHA DO FUNCIONÁRIO    ")
# print("=============================")
# print(f"Nome   : {nome}")
# print(f"Cargo  : {cargo}")
# print(f"Salário: R$ {salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
# print(f"Tempo  : {anos_empresa} ano(s) de empresa")
# print("=============================")

#====================================

# Exercicio 12

# peso = float(input("Digite seu peso em kg: "))
# altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# imc = peso / (altura ** 2)

# print(f"Seu IMC é de {imc:.2f}.")

#====================================

# Exercicio 13

# Definindo dois números para teste de forma estática (pode ser alterado)
# num1 = 120
# num2 = -5

# print(f"O primeiro número é maior que o segundo? {num1 > num2}")
# print(f"Os dois são iguais? {num1 == num2}")
# print(f"Ambos são positivos? {num1 > 0 and num2 > 0}")
# print(f"Pelo menos um é maior que 100? {num1 > 100 or num2 > 100}")
# print(f"O primeiro é diferente de zero? {num1 != 0}")

#====================================

# Exercicio 14

# # Cenário Inicial
# a = 10
# b = 20

# # 1ª Forma: Utilizando variável auxiliar
# aux = a
# a = b
# b = aux
# print(f"Forma Auxiliar - a: {a}, b: {b}")

# # Resetando os valores para o teste da segunda forma
# a = 10
# b = 20

# # 2ª Forma: Método idiomático do Python (Atribuição Múltipla / Tuple Unpacking)
# a, b = b, a
# print(f"Forma Idiomática - a: {a}, b: {b}")

#====================================

# Exercicio 15

# valor_compra = float(input("Digite o valor total da compra: R$ "))

# desconto = valor_compra * 0.10
# valor_final = valor_compra - desconto

# print(f"Valor original: R$ {valor_compra:.2f}")
# print(f"Desconto (10%): R$ {desconto:.2f}")
# print(f"Valor final a pagar: R$ {valor_final:.2f}")

# #====================================

# # Exercicio 16

# import math

# # Definição dos pontos como tuplas
# p1 = (3, 4)
# p2 = (7, 1)

# # Aplicação da fórmula da distância euclidiana
# distancia = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# print(f"A distância entre os pontos P1 e P2 é: {distancia:.4f}")

# #====================================

# # Exercicio 17

# produto = input("Descrição do produto: ")
# quantidade = int(input("Quantidade: "))
# preco_unitario = float(input("Preço unitário: R$ "))

# subtotal = quantidade * preco_unitario
# imposto = subtotal * 0.12
# total = subtotal + imposto

# print("\n===== NOTA FISCAL =====")
# print(f"Produto   : {produto}")
# print(f"Quantidade: {quantidade} unidade(s)")
# print(f"Preço Unit: R$ {preco_unitario:.2f}")
# print(f"Subtotal  : R$ {subtotal:.2f}")
# print(f"Imposto   : R$ {imposto:.2f}")
# print(f"Total     : R$ {total:.2f}")
# print("=======================")

# #====================================

# # Exercicio 18

# metros = float(input("Digite a distância em metros: "))

# # Fatores de conversão constantes
# FATOR_POLEGADAS = 39.3701
# FATOR_PES = 3.28084

# km = metros / 1000
# cm = metros * 100
# mm = metros * 1000
# polegadas = metros * FATOR_POLEGADAS
# pes = metros * FATOR_PES

# # Tabela formatada usando alinhamentos por f-string
# print(f"\n{'Unidade':<12} | {'Valor Formatado':>15}")
# print("-" * 30)
# print(f"{'Quilômetros':<12} | {km:>15.4f} km")
# print(f"{'Centímetros':<12} | {cm:>15.2f} cm")
# print(f"{'Milímetros':<12} | {mm:>15.2f} mm")
# print(f"{'Polegadas':<12} | {polegadas:>15.2f} in")
# print(f"{'Pés':<12} | {pes:>15.2f} ft")

# #====================================


# # Exercicio 19

# email_bruto = "   joao.silva@EMPRESA.com.br   "

# # Limpeza e tratamento inicial de strings
# email_limpo = email_bruto.strip()
# email_normalizado = email_limpo.lower()

# # Separação usando a partição ou split
# usuario, dominio = email_normalizado.split("@")

# print(f"E-mail limpo e normalizado: '{email_normalizado}'")
# print(f"Nome de usuário extraído  : '{usuario}'")
# print(f"Domínio extraído          : '{dominio}'")

# #====================================


# # Exercicio 20

# capital = float(input("Capital inicial investido: R$ "))
# taxa_mensal_percentual = float(input("Taxa de juros ao mês (%): "))
# periodo_meses = int(input("Período da aplicação (em meses): "))

# # Conversão da taxa percentual para decimal
# i = taxa_mensal_percentual / 100

# montante_final = capital * (1 + i * periodo_meses)
# juros_totais = montante_final - capital

# print("\n--- RESUMO DO INVESTIMENTO ---")
# print(f"Capital Inicial   : R$ {capital:.2f}")
# print(f"Taxa de Juros     : {taxa_mensal_percentual:.2f}% ao mês")
# print(f"Período           : {periodo_meses} meses")
# print(f"Juros Acumulados  : R$ {juros_totais:.2f}")
# print(f"Montante Final    : R$ {montante_final:.2f}")

# #====================================


# # Exercicio 21

# def saudacao(nome: str) -> str:
#     """Retorna uma mensagem de boas-vindas personalizada.

#     Args:
#         nome (str): Nome da pessoa a ser saudada.

#     Returns:
#         str: String com a mensagem de boas-vindas.

#     Example:
#         >>>saudacao("Ana")
#         'Olá, Ana! Seja bem-vinda ao curso.'
#     """
#     return f"Olá, {nome}! Seja bem-vindo(a) ao curso."

# # Chamadas de teste exigidas
# print(saudacao("Leonam"))
# print(saudacao("Carlos"))
# print(saudacao("Beatriz"))

# #====================================

# # Exercicio 22

# def calcular_area(largura: float, altura: float) -> float:
#     return largura * altura

# def formatar_nome(nome: str, sobrenome: str) -> str:
#     return f"{nome} {sobrenome}".title()

# def eh_maior_de_idade(idade: int) -> bool:
#     return idade >= 18

# #====================================


# # Exercicio 23   

# import json

# aluno = {
#     "nome": "Pedro Henrique",
#     "idade": 22,
#     "curso": "Full Stack",
#     "ativo": True,
#     "notas": [8.5, 9.0, 7.5]
# }

# # Serialização para string JSON
# aluno_json_string = json.dumps(aluno, indent=2, ensure_ascii=False)
# print("--- String JSON Gerada ---")
# print(aluno_json_string)

# # Desserialização de volta para dicionário Python
# aluno_dict = json.loads(aluno_json_string)
# media_notas = sum(aluno_dict["notas"]) / len(aluno_dict["notas"])

# print("\n--- Dados Extraídos ---")
# print(f"Nome do Aluno: {aluno_dict['nome']}")
# print(f"Média Final  : {media_notas:.2f}")

# #====================================


# # Exercicio 24

# from typing import Tuple

# def converter_moeda(valor_brl: float) -> Tuple[float, float]:
#     """Converte um valor monetário em Reais (BRL) para Dólar (USD) e Euro (EUR).

#     Utiliza as cotações fixas de 1 USD = 5.15 BRL e 1 EUR = 5.58 BRL.

#     Args:
#         valor_brl (float): O montante financeiro em Reais a ser convertido.

#     Returns:
#         Tuple[float, float]: Uma tupla contendo o valor em USD e EUR, respectivamente.

#     Example:
#         >>> converter_moeda(100.0)
#         (19.41747572815534, 17.92114695340502)
#     """
#     cotacao_usd = 5.15
#     cotacao_eur = 5.58
    
#     valor_usd = valor_brl / cotacao_usd
#     valor_eur = valor_brl / cotacao_eur
#     return valor_usd, valor_eur

# # Teste prático da função
# usd, eur = converter_moeda(250.00)
# print(f"R$ 250,00 equivalem a: $ {usd:.2f} USD e € {eur:.2f} EUR")

# #====================================

# # Exercicio 25

# import json

# produto_ecommerce = {
#     "id": 101,
#     "nome": "Teclado Mecânico RGB",
#     "preco": 349.90,
#     "estoque": 42,
#     "disponivel": True,
#     "categorias": ["Periféricos", "Informática", "Gamer"]
# }

# # Escrita em arquivo estruturado JSON
# with open("produto.json", "w", encoding="utf-8") as f:
#     json.dump(produto_ecommerce, f, indent=2, ensure_ascii=False)

# # Leitura do arquivo salvo
# with open("produto.json", "r", encoding="utf-8") as f:
#     produto_carregado = json.load(f)

# print("--- Dados do Produto Cadastrado ---")
# for chave, valor in produto_carregado.items():
#     print(f"{chave.title():<12}: {valor}")

# #====================================

# # Exercicio 26

# from typing import Union, Optional, Dict, Any

# def buscar_usuario(id_usuario: int, nome_usuario: Union[str, None]) -> Optional[Dict[str, Any]]:
#     """Busca dados estruturados de um usuário pelo identificador numérico e nome.

#     Args:
#         id_usuario (int): Identificador numérico único do usuário.
#         nome_usuario (Union[str, None]): Nome ou string identificadora, aceita Nulo.

#     Returns:
#         Optional[Dict[str, Any]]: Dicionário com registros de dados ou None caso o ID seja inválido.
#     """
#     if id_usuario < 0:
#         return None
        
#     return {
#         "id": id_usuario,
#         "nome": nome_usuario if nome_usuario is not None else "Usuário Anônimo",
#         "status": "Ativo"
#     }

# # Executando testes controlados
# print(buscar_usuario(42, "Leonam de Sousa"))
# print(buscar_usuario(-1, "Invalido"))

# #====================================

# # Exercicio 27

# import json

# equipe = [
#     {"nome": "Alice Abreu", "cargo": "Dev Backend", "salario": 8500.00, "departamento": "TI"},
#     {"nome": "Bruno Borges", "cargo": "Dev Frontend", "salario": 7200.00, "departamento": "TI"},
#     {"nome": "Carla Costa", "cargo": "Product Owner", "salario": 9800.00, "departamento": "Produtos"}
# ]

# # Salvando a lista de dicionários
# with open("funcionarios.json", "w", encoding="utf-8") as f:
#     json.dump(equipe, f, indent=2, ensure_ascii=False)

# # Carregando os registros salvos
# with open("funcionarios.json", "r", encoding="utf-8") as f:
#     funcionarios_carregados = json.load(f)

# # Exibição tabulada e cálculo de médias
# print(f"{'Nome':<15} | {'Cargo':<15} | {'Salário':<10}")
# print("-" * 48)
# soma_salarios = 0.0

# for func in funcionarios_carregados:
#     print(f"{func['nome']:<15} | {func['cargo']:<15} | R$ {func['salario']:>8.2f}")
#     soma_salarios += func['salario']

# salario_medio = soma_salarios / len(funcionarios_carregados)
# print("-" * 48)
# print(f"Salário Médio da Equipe: R$ {salario_medio:.2f}")

# #====================================

# # Exercicio 28

# def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
#     """Calcula o montante acumulado por juros compostos.

#     Args:
#         capital (float): Valor inicial do investimento principal.
#         taxa (float): Taxa de juros expressa em valor percentual (ex: 5 para 5%).
#         periodo (int): Tempo de aplicação expresso em número de meses/anos.

#     Returns:
#         float: Montante financeiro total acumulado no fim do período.

#     Raises:
#         ValueError: Ocorre se o capital inicial ou a taxa de juros informada for menor que zero.

#     Example:
#         >>> calcular_juros_compostos(1000.0, 10.0, 2)
#         1210.0
#     """
#     if capital < 0 or taxa < 0:
#         raise ValueError("O capital e a taxa de juros não podem assumir valores negativos.")
#     return capital * (1 + taxa / 100) ** periodo

# #====================================


# # Exercicio 29

# import json

# resposta_api = """{
#     "cidade": "Manaus",
#     "pais": "BR",
#     "temperatura": {
#         "atual": 32.4,
#         "minima": 26.1,
#         "maxima": 35.8,
#         "sensacao": 38.2
#     },
#     "umidade": 87,
#     "condicao": "Parcialmente nublado",
#     "vento": { "velocidade_kmh": 12, "direcao": "NE" },
#     "atualizado_em": "2025-01-15T14:30:00"
# }"""

# dados_clima = json.loads(resposta_api)

# print(f"===== BOLETIM METEOROLÓGICO: {dados_clima['cidade'].upper()} ({dados_clima['pais']}) =====")
# print(f"Condição Atual : {dados_clima['condicao']}")
# print(f"Temperatura    : {dados_clima['temperatura']['atual']}°C (Sensação de {dados_clima['temperatura']['sensacao']}°C)")
# print(f"Extremas do Dia: Mínima de {dados_clima['temperatura']['minima']}°C | Máxima de {dados_clima['temperatura']['maxima']}°C")
# print(f"Umidade Relativa: {dados_clima['umidade']}%")
# print(f"Vento          : {dados_clima['vento']['velocidade_kmh']} km/h na direção {dados_clima['vento']['direcao']}")
# print("==================================================")

# #====================================

# # Exercicio 30

# import json
# from typing import TypedDict, List

# class ItemPedido(TypedDict):
#     produto: str
#     quantidade: int
#     preco_unitario: float

# class Pedido(TypedDict):
#     id_pedido: int
#     cliente: str
#     itens: List[ItemPedido]
#     status: str

# # Instanciação rigorosa utilizando a estrutura tipada definida
# meu_pedido: Pedido = {
#     "id_pedido": 4501,
#     "cliente": "Leonam Silva",
#     "itens": [
#         {"produto": "Mouse Gamer", "quantidade": 1, "preco_unitario": 189.90},
#         {"produto": "Mousepad Extendido", "quantidade": 2, "preco_unitario": 59.90}
#     ],
#     "status": "Processando Faturamento"
# }

# pedido_json = json.dumps(meu_pedido, indent=2, ensure_ascii=False)
# print(pedido_json)

# #====================================

# # Exercicio 31

# import json

# cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
# perfil = {"id": 1042, "cargo": "Engenheira de Software", "nivel": "Senior", "salario": 12500.00, "habilidades": ["Python", "Django", "PostgreSQL"]}

# # Mesclando dicionários utilizando o operador unpacking (**)
# funcionario_completo = {**cadastro, **perfil}

# with open("funcionario_completo.json", "w", encoding="utf-8") as f:
#     json.dump(funcionario_completo, f, indent=2, ensure_ascii=False)

# # Carregando e exibindo formatado
# with open("funcionario_completo.json", "r", encoding="utf-8") as f:
#     dados_f = json.load(f)

# print(f"Funcionário: {dados_f['nome']} | Cargo: {dados_f['cargo']} ({dados_f['nivel']})")
# print("Habilidades Técnicas Registradas:")
# for i, habilidade in enumerate(dados_f["habilidades"], 1):
#     print(f"  {i}. {habilidade}")

# #====================================

# # Exercicio 32

# from typing import Dict, List, Any

# def validar_cadastro(dados: Dict[str, Any]) -> Dict[str, List[str]]:
#     """Valida campos de um cadastro de usuário aplicando regras específicas de negócio.

#     Args:
#         dados (Dict[str, Any]): Dicionário com informações cruciais do candidato.

#     Returns:
#         Dict[str, List[str]]: Dicionário contendo lista de validações bem-sucedidas ou falhas.
#     """
#     erros: List[str] = []
#     validos: List[str] = []

#     # Validação do Nome
#     nome = dados.get("nome", "")
#     if len(nome) >= 3:
#         validos.append("nome")
#     else:
#         erros.append("Nome deve possuir pelo menos 3 caracteres.")

#     # Validação de E-mail
#     email = dados.get("email", "")
#     if "@" in email and "." in email:
#         validos.append("email")
#     else:
#         erros.append("Formato de E-mail inválido.")

#     # Validação da Idade
#     idade = dados.get("idade", 0)
#     if 18 <= id and idade <= 120:
#         validos.append("idade")
#     else:
#         erros.append("Idade permitida fora dos limites (18 a 120 anos).")

#     # Validação de CPF
#     cpf = str(dados.get("cpf", ""))
#     if cpf.isdigit() and len(cpf) == 11:
#         validos.append("cpf")
#     else:
#         erros.append("O CPF deve conter exatamente 11 dígitos estritamente numéricos.")

#     return {"valido": validos, "erros": erros}

# # Testes Práticos
# usuario_valido = {"nome": "Leo", "email": "leo@test.com", "idade": 23, "cpf": "12345678901"}
# usuario_invalido = {"nome": "An", "email": "email_errado", "idade": 15, "cpf": "123"}

# print("Teste Válido   :", validar_cadastro(usuario_valido))
# print("Teste Inválido :", validar_cadastro(usuario_invalido))

# #====================================

# # Exercicio 33

# import json
# from datetime import datetime
# from typing import List, Dict, Any

# def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None:
#     """Registra uma ocorrência de evento com data e hora em formato ISO."""
#     try:
#         with open(arquivo, "r", encoding="utf-8") as f:
#             logs = json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         logs = []

#     novo_log = {
#         "timestamp": datetime.now().isoformat(),
#         "nivel": nivel.upper(),
#         "mensagem": mensagem
#     }
#     logs.append(novo_log)

#     with open(arquivo, "w", encoding="utf-8") as f:
#         json.dump(logs, f, indent=2, ensure_ascii=False)

# def ler_logs(arquivo: str) -> List[Dict[str, Any]]:
#     """Carrega todos os logs de eventos salvos."""
#     try:
#         with open(arquivo, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# def filtrar_por_nivel(logs: List[Dict[str, Any]], nivel: str) -> List[Dict[str, Any]]:
#     """Filtra ocorrências baseado em gravidade do log."""
#     return [log for log in logs if log["nivel"] == nivel.upper()]

# # Demonstração Prática
# arq_log = "sistema_eventos.json"
# registrar_evento(arq_log, "INFO", "Inicialização da API de eventos")
# registrar_evento(arq_log, "WARNING", "Uso elevado de memória RAM detectado (>85%)")
# registrar_evento(arq_log, "ERROR", "Falha de conexão com Banco de Dados")
# registrar_evento(arq_log, "INFO", "Limpeza de conexões mortas executada")
# registrar_evento(arq_log, "ERROR", "Autenticação rejeitada para usuário admin")

# todos_logs = ler_logs(arq_log)
# erros_filtrados = filtrar_por_nivel(todos_logs, "ERROR")

# print(f"Total de Erros Críticos Encontrados: {len(erros_filtrados)}")
# print(json.dumps(erros_filtrados, indent=2))

# #====================================

# # Exercicio 34

# import json
# from typing import Any, Dict

# # Criando o arquivo de configurações mockado para o teste
# config_data = {
#     "app": {"versao": "1.0.0", "modo": "production"},
#     "banco": {"host": "localhost", "porta": 5432},
#     "email": {"servidor": "smtp.gmail.com"}
# }
# with open("config.json", "w") as f:
#     json.dump(config_data, f, indent=2)

# def carregar_config(caminho: str) -> Dict[str, Any]:
#     with open(caminho, "r", encoding="utf-8") as f:
#         return json.load(f)

# def obter_valor(config: Dict[str, Any], chave: str, padrao: Any = None) -> Any:
#     """Navega por chaves aninhadas usando notação de ponto."""
#     partes = chave.split(".")
#     objeto_atual = config
    
#     for parte in partes:
#         if isinstance(objeto_atual, dict) and parte in objeto_atual:
#             objeto_atual = objeto_atual[parte]
#         else:
#             return padrao
#     return objeto_atual

# # Demonstração com 5 chamadas exigidas
# configuracao = carregar_config("config.json")
# print("1. Versão do App :", obter_valor(configuracao, "app.versao"))
# print("2. Modo do App    :", obter_valor(configuracao, "app.modo"))
# print("3. Host do Banco  :", obter_valor(configuracao, "banco.host"))
# print("4. Porta do Banco :", obter_valor(configuracao, "banco.porta"))
# print("5. Chave Inexist. :", obter_valor(configuracao, "banco.senha", "Default123"))

# #====================================

# # Exercicio 35

# import json
# from typing import List, Dict, Any

# vendas_json = """[
#     {"mes": "Janeiro",  "produto": "Notebook", "quantidade": 45, "valor_unit": 3200.00},
#     {"mes": "Janeiro",  "produto": "Mouse",    "quantidade": 120, "valor_unit": 89.90},
#     {"mes": "Fevereiro","produto": "Notebook", "quantidade": 38, "valor_unit": 3200.00},
#     {"mes": "Fevereiro","produto": "Teclado",  "quantidade": 75, "valor_unit": 149.90},
#     {"mes": "Março",    "produto": "Monitor",  "quantidade": 30, "valor_unit": 1200.00},
#     {"mes": "Março",    "produto": "Mouse",    "quantidade": 200,"valor_unit": 89.90}
# ]"""

# lista_vendas = json.loads(vendas_json)

# def calcular_total_mes(vendas: List[Dict[str, Any]], mes: str) -> float:
#     return sum(item["quantidade"] * item["valor_unit"] for item in vendas if item["mes"].lower() == mes.lower())

# def produto_mais_vendido(vendas: List[Dict[str, Any]]) -> str:
#     contagem_produtos: Dict[str, int] = {}
#     for item in vendas:
#         prod = item["produto"]
#         contagem_produtos[prod] = contagem_produtos.get(prod, 0) + item["quantidade"]
#     return max(contagem_produtos, key=contagem_produtos.get) # type: ignore

# def receita_total(vendas: List[Dict[str, Any]]) -> float:
#     return sum(item["quantidade"] * item["valor_unit"] for item in vendas)

# # Exibindo Resultados dos cálculos analíticos
# print(f"Faturamento Total de Janeiro: R$ {calcular_total_mes(lista_vendas, 'Janeiro'):.2f}")
# print(f"Produto Líder em Volume de Venda: {produto_mais_vendido(lista_vendas)}")
# print(f"Receita Líquida Total Acumulada: R$ {receita_total(lista_vendas):.2f}")

# #====================================

# # Exercicio 36

# import json
# from typing import List, Dict, Optional

# ARQUIVO_CONTATOS = "contatos.json"

# def _salvar_arquivo(contatos: List[Dict[str, str]]) -> None:
#     with open(ARQUIVO_CONTATOS, "w", encoding="utf-8") as f:
#         json.dump(contatos, f, indent=2, ensure_ascii=False)

# def listar_contatos() -> List[Dict[str, str]]:
#     try:
#         with open(ARQUIVO_CONTATOS, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# def adicionar_contato(nome: str, telefone: str, email: str) -> None:
#     contatos = listar_contatos()
#     contatos.append({"nome": nome, "telefone": telefone, "email": email})
#     _salvar_arquivo(contatos)

# def buscar_contato(nome: str) -> Optional[Dict[str, str]]:
#     contatos = listar_contatos()
#     for c in contatos:
#         if c["nome"].lower() == nome.lower():
#             return c
#     return None

# def remover_contato(nome: str) -> bool:
#     contatos = listar_contatos()
#     tamanho_original = len(contatos)
#     contatos = [c for c in contatos if c["nome"].lower() != nome.lower()]
#     _salvar_arquivo(contatos)
#     return len(contatos) < tamanho_original

# # Execução das 4 Operações solicitadas na demonstração
# adicionar_contato("Leonam Silva", "9599999-9999", "leonam@dev.com")
# adicionar_contato("Maria Oliveira", "1198888-8888", "maria@teste.com")
# adicionar_contato("Carlos Souza", "2197777-7777", "carlos@corp.com")

# print("Contatos Listados:", listar_contatos())
# print("Resultado Busca Leonam:", buscar_contato("Leonam Silva"))
# print("Removendo Maria Oliveira:", remover_contato("Maria Oliveira"))
# print("Nova Lista de Contatos:", listar_contatos())

# #====================================

# # Exercicio 37 

# from typing import TypeVar, List, Callable

# T = TypeVar('T')
# R = TypeVar('R')

# def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
#     """Aplica uma função de transformação de dados de modo genérico a uma lista."""
#     return [funcao(item) for item in dados]

# # Demonstração 1: Strings -> Maiúsculas
# strings = ["python", "typing", "generics"]
# res_str = aplicar_transformacao(strings, lambda x: x.upper())
# print("Transformação 1 (Strings):", res_str)

# # Demonstração 2: Floats -> Arredondamento com 2 casas decimais
# floats = [3.14159, 2.71828, 1.41421]
# res_float = aplicar_transformacao(floats, lambda x: round(x, 2))
# print("Transformação 2 (Floats) :", res_float)

# # Demonstração 3: Dicionários -> Extraindo um campo específico
# usuarios = [{"id": 1, "nome": "Leo"}, {"id": 2, "nome": "Ana"}]
# res_dict = aplicar_transformacao(usuarios, lambda x: x["nome"])
# print("Transformação 3 (Campos) :", res_dict)

#====================================

# Exercicio 38 

# from typing import TypeVar, List, Callable

# T = TypeVar('T')
# R = TypeVar('R')

# def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
#     """Aplica uma função de transformação de dados de modo genérico a uma lista."""
#     return [funcao(item) for item in dados]

# # Demonstração 1: Strings -> Maiúsculas
# strings = ["python", "typing", "generics"]
# res_str = aplicar_transformacao(strings, lambda x: x.upper())
# print("Transformação 1 (Strings):", res_str)

# # Demonstração 2: Floats -> Arredondamento com 2 casas decimais
# floats = [3.14159, 2.71828, 1.41421]
# res_float = aplicar_transformacao(floats, lambda x: round(x, 2))
# print("Transformação 2 (Floats) :", res_float)

# # Demonstração 3: Dicionários -> Extraindo um campo específico
# usuarios = [{"id": 1, "nome": "Leo"}, {"id": 2, "nome": "Ana"}]
# res_dict = aplicar_transformacao(usuarios, lambda x: x["nome"])
# print("Transformação 3 (Campos) :", res_dict)

#====================================

# Exercicio 39
 
# import json
# from typing import List, Dict

# # String JSON Inicial desordenada para simular carregamento externo
# massa_dados_bruta = """[
#     {"nome": "   joao SILVA ", "email": "JOAO@EMAIL.COM", "telefone": "95991112222"},
#     {"nome": "ana costA   ", "email": "ANA@COSTA.NET", "telefone": "11988887777"}
# ]"""

# def carregar_dados_string(json_str: str) -> List[Dict[str, str]]:
#     return json.loads(json_str)

# def normalizar_dados(dados: List[Dict[str, str]]) -> List[Dict[str, str]]:
#     for item in dados:
#         item["nome"] = item["nome"].strip().title()
#         item["email"] = item["email"].strip().lower()
#     return dados

# def enriquecer_dados(dados: List[Dict[str, str]]) -> List[Dict[str, str]]:
#     for item in dados:
#         # Formatação de telefone simplificada para padrão (XX) XXXXX-XXXX
#         tel = item["telefone"]
#         if len(tel) == 11:
#             item["telefone_formatado"] = f"({tel[:2]}) {tel[2:7]}-{tel[7:]}"
#         else:
#             item["telefone_formatado"] = tel
#     return dados

# def exportar_resultado(dados: List[Dict[str, str]], caminho: str) -> None:
#     with open(caminho, "w", encoding="utf-8") as f:
#         json.dump(dados, f, indent=2, ensure_ascii=False)

# # Execução ordenada do Pipeline
# dados_brutos = carregar_dados_string(massa_dados_bruta)
# dados_normalizados = normalizar_dados(dados_brutos)
# dados_enriquecidos = enriquecer_dados(dados_normalizados)
# exportar_resultado(dados_enriquecidos, "clientes_tratados.json")

# print("Pipeline executado com sucesso! Veja o arquivo 'clientes_tratados.json'")

# #====================================

# # Exercicio 40 

# import json
# from typing import List, Dict, Optional, Any

# ARQUIVO_ALUNOS = "alunos.json"

# def cadastrar_aluno(nome: str, email: str, idade: int, notas: List[float]) -> Dict[str, Any]:
#     """Cadastra um novo aluno no sistema com persistência em JSON.

#     Args:
#         nome (str): Nome completo do discente.
#         email (str): Endereço eletrônico para comunicações.
#         idade (int): Idade cronológica do aluno.
#         notas (List[float]): Lista contendo notas das avaliações do aluno.

#     Returns:
#         Dict[str, Any]: Dicionário estruturado representando o aluno criado.
#     """
#     alunos = listar_alunos()
    
#     # Geração de ID autoincremental
#     novo_id = max([aluno["id"] for aluno in alunos], default=0) + 1
    
#     novo_aluno: Dict[str, Any] = {
#         "id": novo_id,
#         "nome": nome,
#         "email": email,
#         "idade": idade,
#         "notas": notas,
#         "ativo": True
#     }
    
#     alunos.append(novo_aluno)
    
#     with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
#         json.dump(alunos, f, indent=2, ensure_ascii=False)
        
#     return novo_aluno

# def listar_alunos() -> List[Dict[str, Any]]:
#     """Recupera a lista completa de alunos cadastrados."""
#     try:
#         with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# def buscar_por_nome(nome: str) -> Optional[Dict[str, Any]]:
#     """Busca um aluno na base através de match parcial no nome."""
#     alunos = listar_alunos()
#     for aluno in alunos:
#         if nome.lower() in aluno["nome"].lower():
#             return aluno
#     return None

# def calcular_media_turma() -> float:
#     """Calcula a média aritmética geral somando todas as notas de todos alunos."""
#     alunos = listar_alunos()
#     if not alunos:
#         return 0.0
    
#     todas_notas: List[float] = []
#     for aluno in alunos:
#         todas_notas.extend(aluno["notas"])
        
#     return sum(todas_notas) / len(todas_notas) if todas_notas else 0.0

# def exportar_relatorio() -> None:
#     """Gera análises estatísticas da turma e exporta para relatorio_turma.json."""
#     alunos = listar_alunos()
#     if not alunos:
#         print("Impossível exportar relatório de uma base de dados vazia.")
#         return

#     # Mapeando médias individuais para descobrir os extremos da turma
#     medias_individuais = []
#     for a in alunos:
#         med_aluno = sum(a["notas"]) / len(a["notas"]) if a["notas"] else 0.0
#         medias_individuais.append({"aluno": a, "media": med_aluno})

#     melhor_estudante = max(medias_individuais, key=lambda x: x["media"])
#     pior_estudante = min(medias_individuais, key=lambda x: x["media"])

#     relatorio = {
#         "total_alunos": len(alunos),
#         "media_geral_turma": calcular_media_turma(),
#         "aluno_com_maior_media": {
#             "nome": melhor_estudante["aluno"]["nome"],
#             "media": melhor_estudante["media"]
#         },
#         "aluno_com_menor_media": {
#             "nome": pior_estudante["aluno"]["nome"],
#             "media": pior_estudante["media"]
#         }
#     }

#     with open("relatorio_turma.json", "w", encoding="utf-8") as f:
#         json.dump(relatorio, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# DEMONSTRAÇÃO OBRIGATÓRIA DOS REQUISITOS DO PORTFÓLIO
# ---------------------------------------------------------------------------
# # 1. Cadastrar 4 alunos
# cadastrar_aluno("Leonam Silva", "leonam@example.com", 21, [9.5, 8.8, 10.0])
# cadastrar_aluno("Ana Paula", "ana@example.com", 22, [7.0, 8.5, 9.0])
# cadastrar_aluno("Carlos Souza", "carlos@example.com", 20, [6.0, 5.5, 7.0])
# cadastrar_aluno("Beatriz Rezende", "beatriz@example.com", 23, [9.8, 9.5, 9.9])

# print("--- 1. Alunos Cadastrados com Sucesso! ---")

# # 2. Listar Alunos
# print("\n--- 2. Lista de Alunos em Base ---")
# for aluno in listar_alunos():
#     print(f"ID: {aluno['id']} | Nome: {aluno['nome']:<16} | Notas: {aluno['notas']}")

# # 3. Buscar um aluno específico
# print("\n--- 3. Busca de Aluno por Nome ('Leonam') ---")
# resultado_busca = buscar_por_nome("Leonam")
# print(resultado_busca)

# # 4. Exibir a média global calculada da turma
# print("\n--- 4. Média Geral Computada da Turma ---")
# print(f"Média: {calcular_media_turma():.2f}")

# # 5. Exportar relatório analítico consolidado
# exportar_relatorio()
# print("\n--- 5. Relatório exportado com sucesso para 'relatorio_turma.json'! ---")

# #====================================
