"""
=============================================================
ATIVIDADES — Registry Pattern em Python
Do fácil ao difícil: 5 desafios em contextos reais

Curso de Capacitação Full Stack – ITEAM
Professor: Msc. Hygo Sousa De Oliveira
=============================================================

INSTRUÇÕES GERAIS:
  1. Leia o código "ANTES" de cada atividade com atenção.
  2. Implemente a solução com Registry na seção indicada.
  3. O comportamento de saída deve ser IDÊNTICO ao original.
  4. Não apague o código "ANTES" — ele serve de referência.
  5. Execute e confira: os prints devem ser os mesmos.

NÍVEIS:
  🟢 Atividade 1 — Básico        (dicionário simples)
  🟢 Atividade 2 — Básico+       (classe Registry)
  🟡 Atividade 3 — Intermediário (decorator + classe)
  🟡 Atividade 4 — Intermediário (Decision Engine)
  🔴 Atividade 5 — Avançado      (Registry completo + plugins)
=============================================================
"""


# ==============================================================
# 🟢 ATIVIDADE 1 — Calculadora de Operações
# Nível: Básico | Conceito: dicionário simples como registry
# ==============================================================

print("=" * 60)
print("ATIVIDADE 1 — Calculadora de Operações")
print("=" * 60)

# ── ANTES (if/elif) ──────────────────────────────────────────
def calcular_antes(operacao: str, a: float, b: float) -> float:
    """Calculadora com if/elif — para ser refatorada."""
    if operacao == "soma":
        return a + b
    elif operacao == "subtracao":
        return a - b
    elif operacao == "multiplicacao":
        return a * b
    elif operacao == "divisao":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero.")
        return a / b
    elif operacao == "potencia":
        return a ** b
    elif operacao == "modulo":
        return a % b
    else:
        raise ValueError(f"Operação desconhecida: {operacao}")

print("\n[ANTES]")
print(calcular_antes("soma",          10, 3))    # → 13
print(calcular_antes("subtracao",     10, 3))    # → 7
print(calcular_antes("multiplicacao", 10, 3))    # → 30
print(calcular_antes("divisao",       10, 4))    # → 2.5
print(calcular_antes("potencia",      2,  8))    # → 256.0
print(calcular_antes("modulo",        10, 3))    # → 1


# ── DEPOIS (Registry) ────────────────────────────────────────
"""
TAREFA:
  1. Crie um dicionário OPERACOES_REGISTRY mapeando
     nome → função (use lambdas ou funções nomeadas).
  2. Implemente calcular_depois() consultando o dicionário.
  3. Mantenha o tratamento de ZeroDivisionError e ValueError.
  4. Adicione uma operação nova: "raiz" (√a) sem tocar em
     calcular_depois() — só adicionando no dicionário.

DICA:
  import math
  OPERACOES_REGISTRY = {
      "soma": lambda a, b: a + b,
      ...
  }
"""

# SUA SOLUÇÃO AQUI ↓↓↓

import math

# Dicionário que mapeia nome da operação → função lambda
OPERACOES_REGISTRY = {
    "soma"      : lambda a, b: a + b,
    "subtracao" : lambda a, b: a - b,
    "multiplicacao" : lambda a, b: a * b,
    "divisao"   : lambda a, b: a / b,
    "potencia"  : lambda a, b: a ** b,
    "modulo"    : lambda a, b: a % b,
    # Desafio extra: raiz de 'a' — sem tocar em calcular_depois()
    "raiz"      : lambda a, b: math.sqrt(a),
}


def calcular_depois(operacao: str, a: float, b: float) -> float:
    # Verifica se a operação existe no dicionário
    if operacao not in OPERACOES_REGISTRY:
        raise ValueError(f"Operação '{operacao}' não existe.")

    # Verifica divisão por zero antes de executar
    if operacao == "divisao" and b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")

    # Consulta o dicionário e executa a função correspondente
    return OPERACOES_REGISTRY[operacao](a, b)


# ─── Demonstração ─────────────────────────────────────────

testes = [
    ("soma",          10, 5),
    ("subtracao",     10, 5),
    ("multiplicacao", 10, 5),
    ("divisao",       10, 5),
    ("potencia",      10, 5),
    ("modulo",        10, 3),
    ("raiz",          25, 0),   # desafio extra
    ("divisao",       10, 0),   # erro: divisão por zero
    ("absurdo",       10, 5),   # erro: operação inexistente
]

print("=" * 40)
for operacao, a, b in testes:
    try:
        resultado = calcular_depois(operacao, a, b)
        print(f"  {operacao:15} ({a}, {b}) = {resultado}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"  ❌ {e}")
print("=" * 40)

# ==============================================================
# 🟢 ATIVIDADE 2 — Sistema de Relatórios
# Nível: Básico+ | Conceito: classe Registry reutilizável
# ==============================================================

print("\n" + "=" * 60)
print("ATIVIDADE 2 — Sistema de Relatórios")
print("=" * 60)

# ── ANTES (if/elif) ──────────────────────────────────────────
def gerar_relatorio_antes(formato: str, dados: dict) -> None:
    """Gerador de relatórios com if/elif — para ser refatorado."""
    if formato == "resumo":
        print(f"[RESUMO] Total de itens: {len(dados)}")
        for k, v in dados.items():
            print(f"  {k}: {v}")

    elif formato == "detalhado":
        print("[DETALHADO] ─────────────────")
        for k, v in dados.items():
            tipo = type(v).__name__
            print(f"  {k:15} | {str(v):20} | tipo: {tipo}")
        print("─────────────────────────────")

    elif formato == "contagem":
        print(f"[CONTAGEM] {len(dados)} campo(s) registrado(s).")

    elif formato == "chaves":
        print(f"[CHAVES] {list(dados.keys())}")

    elif formato == "valores":
        print(f"[VALORES] {list(dados.values())}")

    else:
        raise ValueError(f"Formato desconhecido: {formato}")


dados_exemplo = {"nome": "Ana", "idade": 28, "cargo": "Dev", "salario": 9000.0}

print("\n[ANTES]")
gerar_relatorio_antes("resumo",    dados_exemplo)
gerar_relatorio_antes("contagem",  dados_exemplo)
gerar_relatorio_antes("chaves",    dados_exemplo)


# ── DEPOIS (Registry com classe) ─────────────────────────────
"""
TAREFA:
  1. Implemente (ou copie do material) a classe Registry.
  2. Crie uma instância: relatorio_registry = Registry()
  3. Extraia cada bloco do if/elif para uma função separada.
  4. Registre cada função no registry.
  5. Implemente gerar_relatorio_depois() sem nenhum if/elif.
  6. Adicione um formato novo "json_pretty" (usando json.dumps)
     apenas adicionando-o ao registry — sem mudar a função principal.

DICA:
  class Registry:
      def __init__(self): self._store = {}
      def register(self, chave, valor): ...
      def get(self, chave): ...
      def __contains__(self, chave): ...
"""

# SUA SOLUÇÃO AQUI ↓↓↓
import json

# ─── Classe Registry reutilizável ─────────────────────────

class Registry:
    def __init__(self):
        # Dicionário interno que guarda nome → função
        self._registro = {}

    def register(self, nome: str, funcao):
        # Cadastra uma nova função no registro
        self._registro[nome] = funcao

    def get(self, nome: str):
        # Retorna a função correspondente ao nome
        return self._registro.get(nome)

    def __contains__(self, nome: str):
        # Permite usar 'in' para verificar se o formato existe
        return nome in self._registro


# ─── Instância global do registry ─────────────────────────

relatorio_registry = Registry()


# ─── Funções de cada formato ──────────────────────────────

def formato_resumo(dados: dict) -> None:
    print("── RESUMO ──────────────────────────")
    print(f"  Total de itens : {dados['total']}")
    print(f"  Média          : {dados['media']:.2f}")
    print(f"  Status         : {dados['status']}")

def formato_detalhado(dados: dict) -> None:
    print("── DETALHADO ───────────────────────")
    for chave, valor in dados.items():
        print(f"  {chave:<15}: {valor}")

def formato_tabela(dados: dict) -> None:
    print("── TABELA ──────────────────────────")
    print(f"  {'CAMPO':<15} {'VALOR':>10}")
    print(f"  {'-'*15} {'-'*10}")
    for chave, valor in dados.items():
        print(f"  {chave:<15} {str(valor):>10}")

def formato_csv(dados: dict) -> None:
    print("── CSV ─────────────────────────────")
    print(",".join(dados.keys()))
    print(",".join(str(v) for v in dados.values()))

def formato_minimalista(dados: dict) -> None:
    print("── MINIMALISTA ─────────────────────")
    print(" | ".join(f"{k}={v}" for k, v in dados.items()))

# Desafio extra: registrando apenas uma nova função, sem tocar em gerar_relatorio_depois()
def formato_json_pretty(dados: dict) -> None:
    print("── JSON PRETTY ─────────────────────")
    print(json.dumps(dados, indent=4, ensure_ascii=False))


# ─── Registra todos os formatos no registry ───────────────

relatorio_registry.register("resumo",       formato_resumo)
relatorio_registry.register("detalhado",    formato_detalhado)
relatorio_registry.register("tabela",       formato_tabela)
relatorio_registry.register("csv",          formato_csv)
relatorio_registry.register("minimalista",  formato_minimalista)
relatorio_registry.register("json_pretty",  formato_json_pretty)  # desafio extra


# ─── Função principal — sem nenhum if/elif ────────────────

def gerar_relatorio_depois(formato: str, dados: dict) -> None:
    # Verifica se o formato existe no registry
    if formato not in relatorio_registry:
        raise ValueError(f"Formato '{formato}' não encontrado no registry.")

    # Busca e executa a função correspondente
    relatorio_registry.get(formato)(dados)


# ─── Demonstração ─────────────────────────────────────────

dados = {
    "total"  : 42,
    "media"  : 8.75,
    "status" : "aprovado"
}

formatos = ["resumo", "detalhado", "tabela", "csv", "minimalista", "json_pretty", "invalido"]

for formato in formatos:
    try:
        gerar_relatorio_depois(formato, dados)
    except ValueError as e:
        print(f"❌ {e}")
    print()

# class Registry: ...

# def _relatorio_resumo(dados: dict) -> None: ...
# def _relatorio_detalhado(dados: dict) -> None: ...
# ...

# relatorio_registry = Registry()
# relatorio_registry.register("resumo", _relatorio_resumo)
# ...

# def gerar_relatorio_depois(formato: str, dados: dict) -> None:
#     ...

# print("\n[DEPOIS]")
# gerar_relatorio_depois("resumo",     dados_exemplo)
# gerar_relatorio_depois("json_pretty", dados_exemplo)  # nova!


# ==============================================================
# 🟡 ATIVIDADE 3 — Pipeline de Validação de Dados
# Nível: Intermediário | Conceito: decorator + Registry + chain
# ==============================================================

print("\n" + "=" * 60)
print("ATIVIDADE 3 — Pipeline de Validação de Dados")
print("=" * 60)

# ── ANTES (if/elif) ──────────────────────────────────────────
def validar_campo_antes(tipo: str, valor) -> tuple[bool, str]:
    """
    Valida um valor conforme seu tipo.
    Retorna (True, "") se válido, (False, mensagem) se inválido.
    """
    if tipo == "email":
        valido = "@" in str(valor) and "." in str(valor).split("@")[-1]
        return (valido, "" if valido else "Email inválido: falta @ ou domínio")

    elif tipo == "cpf":
        digitos = "".join(c for c in str(valor) if c.isdigit())
        valido  = len(digitos) == 11
        return (valido, "" if valido else f"CPF inválido: esperado 11 dígitos, got {len(digitos)}")

    elif tipo == "telefone":
        digitos = "".join(c for c in str(valor) if c.isdigit())
        valido  = len(digitos) in (10, 11)
        return (valido, "" if valido else "Telefone inválido: esperado 10 ou 11 dígitos")

    elif tipo == "cep":
        digitos = "".join(c for c in str(valor) if c.isdigit())
        valido  = len(digitos) == 8
        return (valido, "" if valido else "CEP inválido: esperado 8 dígitos")

    elif tipo == "idade":
        try:
            idade  = int(valor)
            valido = 0 <= idade <= 120
            return (valido, "" if valido else f"Idade inválida: {idade} fora de [0, 120]")
        except (ValueError, TypeError):
            return (False, f"Idade inválida: '{valor}' não é inteiro")

    elif tipo == "nome":
        valido = isinstance(valor, str) and len(valor.strip()) >= 2
        return (valido, "" if valido else "Nome inválido: mínimo 2 caracteres")

    else:
        return (False, f"Tipo de validação desconhecido: '{tipo}'")


print("\n[ANTES]")
casos = [
    ("email",    "ana@iteam.com"),
    ("email",    "invalido_sem_arroba"),
    ("cpf",      "123.456.789-01"),
    ("cpf",      "123"),
    ("telefone", "(92) 98765-4321"),
    ("idade",    25),
    ("idade",    200),
    ("cep",      "69000-000"),
]
for tipo, valor in casos:
    ok, msg = validar_campo_antes(tipo, valor)
    status  = "✅" if ok else "❌"
    print(f"  {status} {tipo:10} | {str(valor):25} | {msg or 'OK'}")


# ── DEPOIS (Registry com decorator) ──────────────────────────
"""
TAREFA:
  1. Crie um Registry e um decorator @registrar_validador("tipo").
  2. Cada validador vira uma função decorada:

       @registrar_validador("email")
       def validar_email(valor) -> tuple[bool, str]:
           ...

  3. Implemente validar_campo_depois() sem if/elif.
  4. DESAFIO: adicione um validador "url" que verifica se o
     valor começa com "http://" ou "https://" e contém "."
     Apenas criando a função — sem tocar em validar_campo_depois().

DICA sobre o decorator:
  validador_registry = Registry()

  def registrar_validador(tipo: str):
      def decorator(func):
          validador_registry.register(tipo, func)
          return func
      return decorator

  @registrar_validador("email")
  def validar_email(valor) -> tuple[bool, str]:
      ...
"""

# SUA SOLUÇÃO AQUI ↓↓↓
import re

# ─── Classe Registry (reutilizada do exercício anterior) ──

class Registry:
    def __init__(self):
        self._registro = {}

    def register(self, nome: str, funcao):
        self._registro[nome] = funcao

    def get(self, nome: str):
        return self._registro.get(nome)

    def __contains__(self, nome: str):
        return nome in self._registro


# ─── Instância global + decorador ─────────────────────────

validador_registry = Registry()

def registrar_validador(tipo: str):
    # Decorador que registra automaticamente a função no registry
    def decorator(func):
        validador_registry.register(tipo, func)
        return func
    return decorator


# ─── Validadores — cada um registrado via decorador ───────

@registrar_validador("email")
def validar_email(valor) -> tuple[bool, str]:
    valor = str(valor)
    valido = "@" in valor and "." in valor.split("@")[-1]
    return (valido, "" if valido else "Email inválido. Ex: nome@dominio.com")


@registrar_validador("cpf")
def validar_cpf(valor) -> tuple[bool, str]:
    # Remove pontos e traços e verifica se tem 11 dígitos numéricos
    cpf = re.sub(r"[.\-]", "", str(valor))
    valido = cpf.isdigit() and len(cpf) == 11
    return (valido, "" if valido else "CPF inválido. Ex: 123.456.789-00")


@registrar_validador("telefone")
def validar_telefone(valor) -> tuple[bool, str]:
    # Remove caracteres especiais e verifica se tem 10 ou 11 dígitos
    tel = re.sub(r"[\s()\-]", "", str(valor))
    valido = tel.isdigit() and len(tel) in (10, 11)
    return (valido, "" if valido else "Telefone inválido. Ex: (92) 99999-9999")


@registrar_validador("cep")
def validar_cep(valor) -> tuple[bool, str]:
    # Remove traço e verifica se tem 8 dígitos numéricos
    cep = re.sub(r"[\-]", "", str(valor))
    valido = cep.isdigit() and len(cep) == 8
    return (valido, "" if valido else "CEP inválido. Ex: 69000-000")


@registrar_validador("idade")
def validar_idade(valor) -> tuple[bool, str]:
    try:
        idade = int(valor)
        valido = 0 <= idade <= 120
        return (valido, "" if valido else "Idade inválida. Deve ser entre 0 e 120.")
    except ValueError:
        return (False, "Idade deve ser um número inteiro.")


@registrar_validador("nome")
def validar_nome(valor) -> tuple[bool, str]:
    # Nome deve ter ao menos duas palavras e só letras/espaços
    partes = str(valor).strip().split()
    valido = len(partes) >= 2 and all(p.isalpha() for p in partes)
    return (valido, "" if valido else "Nome inválido. Digite nome e sobrenome.")


# Desafio extra: novo validador sem tocar em validar_campo_depois()
@registrar_validador("url")
def validar_url(valor) -> tuple[bool, str]:
    valor = str(valor).strip()
    valido = valor.startswith("http://") or valor.startswith("https://")
    return (valido, "" if valido else "URL inválida. Deve começar com http:// ou https://")


# ─── Função principal — sem nenhum if/elif ────────────────

def validar_campo_depois(tipo: str, valor) -> tuple[bool, str]:
    # Verifica se o tipo de validador existe no registry
    if tipo not in validador_registry:
        raise ValueError(f"Tipo '{tipo}' não possui validador registrado.")

    # Busca e executa o validador correspondente
    return validador_registry.get(tipo)(valor)


# ─── Demonstração ─────────────────────────────────────────

formulario = {
    "email"    : ["ana@email.com",     "email_invalido"],
    "cpf"      : ["123.456.789-00",    "1234"],
    "telefone" : ["(92) 99999-9999",   "123"],
    "cep"      : ["69000-000",         "1234"],
    "idade"    : [25,                   200],
    "nome"     : ["Ana Lima",          "Ana"],
    "url"      : ["https://iteam.com", "iteam.com"],
}

for tipo, valores in formulario.items():
    print(f"\n── {tipo.upper()} {'─' * (32 - len(tipo))}")
    for valor in valores:
        valido, mensagem = validar_campo_depois(tipo, valor)
        status = "✅" if valido else "❌"
        erro = f" → {mensagem}" if mensagem else ""
        print(f"  {status} {str(valor):<25}{erro}")

# ==============================================================
# 🟡 ATIVIDADE 4 — Motor de Descontos de E-commerce
# Nível: Intermediário | Conceito: Decision Engine + Registry
# ==============================================================

print("\n" + "=" * 60)
print("ATIVIDADE 4 — Motor de Descontos de E-commerce")
print("=" * 60)

# ── ANTES (if/elif aninhado) ──────────────────────────────────
from dataclasses import dataclass as dc

@dc
class Carrinho:
    valor_total:    float
    cupom:          str | None
    tipo_cliente:   str    # "novo", "fiel", "vip"
    dia_semana:     int    # 0=seg … 6=dom
    quantidade_itens: int


def calcular_desconto_antes(carrinho: Carrinho) -> tuple[float, str]:
    """
    Calcula o desconto e retorna (percentual, motivo).
    Complexidade ciclomática alta — difícil de testar e manter.
    """
    if carrinho.cupom == "BLACKFRIDAY":
        return (0.30, "Cupom Black Friday: 30%")

    elif carrinho.cupom == "BEMVINDO10":
        if carrinho.tipo_cliente != "novo":
            return (0.0, "Cupom BEMVINDO10 apenas para novos clientes")
        return (0.10, "Cupom de boas-vindas: 10%")

    elif carrinho.tipo_cliente == "vip":
        if carrinho.valor_total >= 500:
            return (0.20, "VIP + compra >= R$500: 20%")
        return (0.10, "VIP: 10% base")

    elif carrinho.tipo_cliente == "fiel":
        if carrinho.quantidade_itens >= 5:
            return (0.15, "Fiel + 5 itens: 15%")
        return (0.08, "Fiel: 8%")

    elif carrinho.dia_semana in (5, 6):   # fim de semana
        if carrinho.valor_total >= 200:
            return (0.12, "FDS + >= R$200: 12%")
        return (0.05, "Fim de semana: 5%")

    elif carrinho.valor_total >= 1000:
        return (0.10, "Compra acima de R$1.000: 10%")

    return (0.0, "Sem desconto aplicável")


carrinhos_teste = [
    Carrinho(800.0, "BLACKFRIDAY", "normal", 2, 3),
    Carrinho(150.0, "BEMVINDO10",  "novo",   1, 1),
    Carrinho(150.0, "BEMVINDO10",  "fiel",   1, 2),
    Carrinho(600.0, None,          "vip",    2, 3),
    Carrinho(100.0, None,          "vip",    1, 0),
    Carrinho(350.0, None,          "fiel",   6, 4),
    Carrinho(350.0, None,          "fiel",   2, 4),
    Carrinho(250.0, None,          "normal", 6, 5),
    Carrinho(80.0,  None,          "normal", 6, 6),
    Carrinho(1200.0,None,          "normal", 4, 1),
    Carrinho(300.0, None,          "normal", 2, 3),
]

print("\n[ANTES]")
for c in carrinhos_teste:
    pct, motivo = calcular_desconto_antes(c)
    valor_desc  = c.valor_total * pct
    print(f"  R$ {c.valor_total:7.2f} | {pct*100:4.0f}% | {motivo}")


# ── DEPOIS (Decision Engine + Registry) ──────────────────────
"""
TAREFA:
  1. Crie um Registry de handlers. Cada handler recebe
     um Carrinho e retorna tuple[float, str].

  2. Crie a função decidir_regra(carrinho: Carrinho) -> str
     — o Decision Engine. Ela contém TODA a lógica condicional
     e retorna apenas uma chave simples como:
         "cupom:blackfriday", "cliente:vip:alto", etc.

  3. Registre um handler para cada chave.

  4. Implemente calcular_desconto_depois() que:
       chave   = decidir_regra(carrinho)
       handler = desconto_registry.get(chave)
       return  handler(carrinho)

  5. DESAFIO: adicione uma nova regra "aniversario_loja" que
     aplica 25% quando dia_semana == 3 (quarta-feira) e
     valor_total >= 300. Adicione SEM tocar em calcular_desconto_depois().

ESTRUTURA SUGERIDA de chaves:
  "cupom:blackfriday"
  "cupom:bemvindo:valido"
  "cupom:bemvindo:invalido"
  "cliente:vip:alto_valor"
  "cliente:vip:padrao"
  "cliente:fiel:muitos_itens"
  "cliente:fiel:padrao"
  "fds:alto_valor"
  "fds:padrao"
  "compra:acima_mil"
  "padrao"
"""

# SUA SOLUÇÃO AQUI ↓↓↓
from dataclasses import dataclass

# ─── Dataclass do Carrinho ────────────────────────────────

@dataclass
class Carrinho:
    valor_total:      float
    cupom:            str | None
    tipo_cliente:     str   # "novo", "fiel", "vip"
    dia_semana:       int   # 0=seg … 6=dom
    quantidade_itens: int


# ─── Classe Registry ──────────────────────────────────────

class Registry:
    def __init__(self):
        self._registro = {}

    def register(self, chave: str, funcao):
        self._registro[chave] = funcao

    def get(self, chave: str):
        return self._registro.get(chave)

    def __contains__(self, chave: str):
        return chave in self._registro


desconto_registry = Registry()

def registrar_desconto(chave: str):
    def decorator(func):
        desconto_registry.register(chave, func)
        return func
    return decorator


# ─── Motor de decisão — toda a lógica condicional aqui ───

def decidir_regra(carrinho: Carrinho) -> str:
    # Cupons têm prioridade máxima
    if carrinho.cupom == "BLACKFRIDAY":
        return "cupom:blackfriday"
    if carrinho.cupom == "BEMVINDO10":
        return "cupom:bemvindo10"

    # Regras por tipo de cliente
    if carrinho.tipo_cliente == "vip":
        if carrinho.valor_total >= 500:
            return "cliente:vip:alto"
        return "cliente:vip:padrao"

    if carrinho.tipo_cliente == "fiel":
        return "cliente:fiel"

    # Desafio extra: aniversário da loja (quarta = dia 2, carrinho >= R$300)
    if carrinho.dia_semana == 2 and carrinho.valor_total >= 300:
        return "aniversario_loja"

    # Regras de fim de semana
    if carrinho.dia_semana in (5, 6):
        return "fds:padrao"

    # Carrinho com muitos itens
    if carrinho.quantidade_itens >= 10:
        return "volume:alto"

    # Nenhuma regra especial aplicável
    return "sem_desconto"


# ─── Manipuladores — um por chave ─────────────────────────

@registrar_desconto("cupom:blackfriday")
def desconto_blackfriday(carrinho: Carrinho) -> tuple[float, str]:
    return (0.40, "🖤 Cupom BLACK FRIDAY — 40% de desconto!")

@registrar_desconto("cupom:bemvindo10")
def desconto_bemvindo(carrinho: Carrinho) -> tuple[float, str]:
    return (0.10, "👋 Cupom BEM-VINDO — 10% de desconto!")

@registrar_desconto("cliente:vip:alto")
def desconto_vip_alto(carrinho: Carrinho) -> tuple[float, str]:
    return (0.30, "⭐ Cliente VIP com carrinho alto — 30% de desconto!")

@registrar_desconto("cliente:vip:padrao")
def desconto_vip_padrao(carrinho: Carrinho) -> tuple[float, str]:
    return (0.20, "⭐ Cliente VIP — 20% de desconto!")

@registrar_desconto("cliente:fiel")
def desconto_fiel(carrinho: Carrinho) -> tuple[float, str]:
    return (0.15, "💛 Cliente Fiel — 15% de desconto!")

@registrar_desconto("fds:padrao")
def desconto_fds(carrinho: Carrinho) -> tuple[float, str]:
    return (0.10, "🎉 Promoção de fim de semana — 10% de desconto!")

@registrar_desconto("volume:alto")
def desconto_volume(carrinho: Carrinho) -> tuple[float, str]:
    return (0.12, "📦 Compra em volume (10+ itens) — 12% de desconto!")

@registrar_desconto("sem_desconto")
def sem_desconto(carrinho: Carrinho) -> tuple[float, str]:
    return (0.0, "Nenhum desconto aplicável.")

# Desafio extra: nova regra sem tocar em calcular_desconto_depois()
@registrar_desconto("aniversario_loja")
def desconto_aniversario(carrinho: Carrinho) -> tuple[float, str]:
    return (0.25, "🎂 Aniversário da Loja na quarta — 25% de desconto!")


# ─── Função principal — apenas 2 linhas ───────────────────

def calcular_desconto_depois(carrinho: Carrinho) -> tuple[float, str]:
    chave = decidir_regra(carrinho)                      # linha 1: motor decide a chave
    return desconto_registry.get(chave)(carrinho)        # linha 2: registry executa o handler


# ─── Demonstração ─────────────────────────────────────────

carrinhos = [
    ("Cupom BLACK FRIDAY",    Carrinho(350.0, "BLACKFRIDAY", "novo",  1, 3)),
    ("Cupom BEM-VINDO",       Carrinho(150.0, "BEMVINDO10",  "novo",  1, 2)),
    ("Cliente VIP alto",      Carrinho(600.0, None,          "vip",   1, 5)),
    ("Cliente VIP padrão",    Carrinho(200.0, None,          "vip",   1, 2)),
    ("Cliente fiel",          Carrinho(250.0, None,          "fiel",  3, 4)),
    ("Fim de semana",         Carrinho(180.0, None,          "novo",  6, 3)),
    ("Compra em volume",      Carrinho(400.0, None,          "novo",  1, 12)),
    ("Aniversário da loja",   Carrinho(350.0, None,          "novo",  2, 4)),
    ("Sem desconto",          Carrinho(100.0, None,          "novo",  1, 2)),
]

print("=" * 55)
print(f"{'🛒 MOTOR DE DESCONTOS':^55}")
print("=" * 55)

for descricao, carrinho in carrinhos:
    percentual, mensagem = calcular_desconto_depois(carrinho)
    economia = carrinho.valor_total * percentual
    total_final = carrinho.valor_total - economia

    print(f"\n📋 {descricao}")
    print(f"   Valor original : R${carrinho.valor_total:.2f}")
    print(f"   {mens

# ==============================================================
# 🔴 ATIVIDADE 5 — Sistema de Processamento de Eventos (Avançado)
# Nível: Avançado | Conceito: Registry completo + múltiplos registries
#                             + tratamento de erros + runtime update
# ==============================================================

print("\n" + "=" * 60)
print("ATIVIDADE 5 — Sistema de Processamento de Eventos")
print("=" * 60)

# ── ANTES (if/elif com lógica de negócio embutida) ───────────
@dc
class Evento:
    tipo:       str
    payload:    dict
    prioridade: int    # 1=baixa, 2=média, 3=alta, 4=crítica
    origem:     str    # "app", "api", "webhook", "cron"


def processar_evento_antes(evento: Evento) -> dict:
    """
    Processador de eventos monolítico.
    Mistura roteamento, lógica de negócio e formatação de resposta.
    """
    resultado = {"evento": evento.tipo, "status": "ok", "acoes": []}

    if evento.tipo == "usuario.criado":
        resultado["acoes"].append("email_boas_vindas enviado")
        resultado["acoes"].append("perfil_inicial criado")
        if evento.payload.get("plano") == "premium":
            resultado["acoes"].append("acesso_premium liberado")

    elif evento.tipo == "usuario.deletado":
        resultado["acoes"].append("dados_pessoais anonimizados")
        resultado["acoes"].append("sessoes_ativas encerradas")
        resultado["acoes"].append("log_auditoria registrado")

    elif evento.tipo == "pagamento.aprovado":
        resultado["acoes"].append("pedido_liberado")
        resultado["acoes"].append("nota_fiscal emitida")
        if evento.prioridade >= 3:
            resultado["acoes"].append("notificacao_prioritaria enviada")

    elif evento.tipo == "pagamento.recusado":
        resultado["acoes"].append("cliente_notificado")
        resultado["acoes"].append("retry_agendado para 1h")
        if evento.payload.get("tentativas", 0) >= 3:
            resultado["status"] = "bloqueado"
            resultado["acoes"].append("conta_suspensa temporariamente")

    elif evento.tipo == "estoque.baixo":
        resultado["acoes"].append("alerta_compras enviado")
        produto = evento.payload.get("produto", "desconhecido")
        qtd     = evento.payload.get("quantidade", 0)
        resultado["acoes"].append(f"reposicao_solicitada: {produto} ({qtd} un)")

    elif evento.tipo == "sistema.erro":
        resultado["status"] = "erro"
        resultado["acoes"].append("log_erro registrado")
        if evento.prioridade == 4:
            resultado["acoes"].append("oncall_acionado via PagerDuty")
            resultado["acoes"].append("rollback_iniciado")

    else:
        resultado["status"] = "ignorado"
        resultado["acoes"].append(f"evento '{evento.tipo}' sem handler registrado")

    return resultado


eventos_teste = [
    Evento("usuario.criado",    {"plano": "premium"},     2, "api"),
    Evento("usuario.criado",    {"plano": "gratuito"},    1, "app"),
    Evento("usuario.deletado",  {"motivo": "solicitação"},2, "app"),
    Evento("pagamento.aprovado",{"valor": 1500.0},        3, "webhook"),
    Evento("pagamento.recusado",{"tentativas": 3},        2, "api"),
    Evento("estoque.baixo",     {"produto": "Notebook", "quantidade": 2}, 3, "cron"),
    Evento("sistema.erro",      {"codigo": 500},          4, "api"),
    Evento("evento.desconhecido",{},                      1, "app"),
]

print("\n[ANTES]")
for ev in eventos_teste:
    res = processar_evento_antes(ev)
    print(f"  [{res['status'].upper():8}] {ev.tipo:25} → {res['acoes']}")


# ── DEPOIS (Registry Completo) ────────────────────────────────
"""
TAREFA (leia com atenção — é o desafio mais completo):

1. CLASSE REGISTRY COMPLETA
   Implemente (ou use a do material) a classe Registry com:
     - register(), get(), update(), unregister()
     - __contains__(), listar_chaves()
     - Tratamento de erros explícito

2. HANDLERS ISOLADOS
   Crie uma função handler para cada tipo de evento.
   Cada handler recebe um Evento e retorna dict.
   Extraia a lógica condicional interna para helpers ou
   mantenha-a dentro do próprio handler.

3. DECORATOR DE REGISTRO
   Crie @registrar_evento("tipo") para auto-registrar
   os handlers ao serem definidos.

4. FUNÇÃO PRINCIPAL SEM if/elif
   def processar_evento_depois(evento: Evento) -> dict:
       try:
           handler = evento_registry.get(evento.tipo)
       except KeyError:
           return {"evento": evento.tipo, "status": "ignorado",
                   "acoes": [f"sem handler para '{evento.tipo}'"]}
       return handler(evento)

5. RUNTIME UPDATE (feature flag simulado)
   Após implementar tudo, simule uma atualização em runtime:
   crie uma versão V2 do handler de "pagamento.aprovado"
   que também envia o evento para um webhook externo,
   e troque usando evento_registry.update(). Demonstre
   que o comportamento muda sem reiniciar o programa.

6. RELATÓRIO FINAL
   Ao final, imprima os eventos registrados:
       print(evento_registry.listar_chaves())

DICA DE ESTRUTURA:
  evento_registry = Registry(nome="EventoRegistry")

  @registrar_evento("usuario.criado")
  def handle_usuario_criado(evento: Evento) -> dict:
      acoes = ["email_boas_vindas enviado", "perfil_inicial criado"]
      if evento.payload.get("plano") == "premium":
          acoes.append("acesso_premium liberado")
      return {"evento": evento.tipo, "status": "ok", "acoes": acoes}

  # ... demais handlers ...

  def processar_evento_depois(evento: Evento) -> dict:
      try:
          handler = evento_registry.get(evento.tipo)
          return handler(evento)
      except KeyError:
          return {"evento": evento.tipo, "status": "ignorado",
                  "acoes": [f"sem handler para '{evento.tipo}'"]}

  # Demonstração de runtime update:
  @registrar_evento("pagamento.aprovado_v2")  # define a v2
  def handle_pagamento_aprovado_v2(evento: Evento) -> dict: ...

  evento_registry.update("pagamento.aprovado", handle_pagamento_aprovado_v2)
  print("\\n[FEATURE FLAG] handler de pagamento.aprovado atualizado em runtime!")
"""

# SUA SOLUÇÃO AQUI ↓↓↓
from dataclasses import dataclass
from datetime import datetime

# ─── Dataclass do Evento ──────────────────────────────────

@dataclass
class Evento:
    tipo:       str
    payload:    dict
    prioridade: int   # 1=baixa … 4=crítica
    origem:     str   # "app", "api", "webhook", "cron"


# ─── Classe Registry completa ─────────────────────────────

class Registry:
    def __init__(self):
        self._registro = {}

    def register(self, chave: str, funcao):
        # Cadastra um novo handler
        self._registro[chave] = funcao
        print(f"  [Registry] ✅ '{chave}' registrado.")

    def get(self, chave: str):
        # Retorna o handler ou lança KeyError se não existir
        if chave not in self._registro:
            raise KeyError(chave)
        return self._registro[chave]

    def update(self, chave: str, funcao):
        # Substitui um handler existente em runtime
        if chave not in self._registro:
            raise KeyError(f"'{chave}' não encontrado para atualização.")
        self._registro[chave] = funcao
        print(f"  [Registry] 🔄 '{chave}' atualizado em runtime.")

    def unregister(self, chave: str):
        # Remove um handler do registry
        if chave not in self._registro:
            raise KeyError(f"'{chave}' não encontrado para remoção.")
        del self._registro[chave]
        print(f"  [Registry] 🗑️  '{chave}' removido.")

    def __contains__(self, chave: str):
        # Permite usar 'in' naturalmente
        return chave in self._registro

    def listar_chaves(self) -> list[str]:
        # Retorna lista com todos os handlers registrados
        return sorted(self._registro.keys())


# ─── Instância global + decorador ─────────────────────────

evento_registry = Registry()

def registrar_evento(tipo: str):
    def decorator(func):
        evento_registry.register(tipo, func)
        return func
    return decorator


# ─── Handlers — um por tipo de evento ────────────────────

@registrar_evento("usuario.criado")
def handle_usuario_criado(evento: Evento) -> dict:
    nome  = evento.payload.get("nome", "desconhecido")
    email = evento.payload.get("email", "—")
    return {
        "acao"     : "conta criada",
        "mensagem" : f"Bem-vindo, {nome}! Confirme seu email: {email}",
        "log"      : f"[{evento.origem.upper()}] Novo usuário: {email}"
    }


@registrar_evento("usuario.deletado")
def handle_usuario_deletado(evento: Evento) -> dict:
    user_id = evento.payload.get("user_id", "?")
    motivo  = evento.payload.get("motivo", "não informado")
    return {
        "acao"     : "conta removida",
        "mensagem" : f"Usuário {user_id} deletado.",
        "log"      : f"Motivo: {motivo} | Prioridade: {evento.prioridade}"
    }


@registrar_evento("pagamento.aprovado")
def handle_pagamento_aprovado(evento: Evento) -> dict:
    valor  = evento.payload.get("valor", 0)
    pedido = evento.payload.get("pedido_id", "?")
    return {
        "acao"     : "pagamento confirmado",
        "mensagem" : f"Pedido {pedido} aprovado — R${valor:.2f}",
        "log"      : f"[V1] Pagamento processado via {evento.origem}"
    }


@registrar_evento("pagamento.recusado")
def handle_pagamento_recusado(evento: Evento) -> dict:
    motivo = evento.payload.get("motivo", "sem saldo")
    cartao = evento.payload.get("cartao", "****")
    return {
        "acao"     : "pagamento negado",
        "mensagem" : f"Cartão {cartao} recusado — {motivo}",
        "log"      : f"Prioridade {evento.prioridade} | origem: {evento.origem}"
    }


@registrar_evento("sistema.erro")
def handle_sistema_erro(evento: Evento) -> dict:
    codigo    = evento.payload.get("codigo", "ERR_000")
    descricao = evento.payload.get("descricao", "erro desconhecido")
    return {
        "acao"     : "erro registrado",
        "mensagem" : f"[{codigo}] {descricao}",
        "log"      : f"🚨 CRÍTICO — origem: {evento.origem} | prioridade: {evento.prioridade}"
    }


@registrar_evento("relatorio.gerado")
def handle_relatorio_gerado(evento: Evento) -> dict:
    tipo    = evento.payload.get("tipo", "geral")
    formato = evento.payload.get("formato", "pdf")
    return {
        "acao"     : "relatório exportado",
        "mensagem" : f"Relatório '{tipo}' gerado em {formato.upper()}",
        "log"      : f"Solicitado via {evento.origem} em {datetime.now().strftime('%H:%M:%S')}"
    }


@registrar_evento("email.enviado")
def handle_email_enviado(evento: Evento) -> dict:
    destinatario = evento.payload.get("para", "?")
    assunto      = evento.payload.get("assunto", "sem assunto")
    return {
        "acao"     : "email disparado",
        "mensagem" : f"Email '{assunto}' enviado para {destinatario}",
        "log"      : f"Origem: {evento.origem} | Prioridade: {evento.prioridade}"
    }


# ─── Função principal ─────────────────────────────────────

def processar_evento_depois(evento: Evento) -> None:
    prioridades = {1: "🟢 baixa", 2: "🟡 média", 3: "🟠 alta", 4: "🔴 crítica"}
    print(f"\n{'─'*50}")
    print(f"  Evento    : {evento.tipo}")
    print(f"  Origem    : {evento.origem} | Prioridade: {prioridades.get(evento.prioridade, '?')}")

    try:
        # Busca e executa o handler correspondente
        resultado = evento_registry.get(evento.tipo)(evento)
        print(f"  Ação      : {resultado['acao']}")
        print(f"  Mensagem  : {resultado['mensagem']}")
        print(f"  Log       : {resultado['log']}")

    except KeyError:
        print(f"  ❌ Nenhum handler registrado para '{evento.tipo}'.")


# ─── Demonstração ─────────────────────────────────────────

print("\n" + "=" * 50)
print(f"{'⚡ SISTEMA DE PROCESSAMENTO DE EVENTOS':^50}")
print("=" * 50)

eventos = [
    Evento("usuario.criado",    {"nome": "Ana Lima", "email": "ana@email.com"},    2, "app"),
    Evento("pagamento.aprovado",{"valor": 349.90, "pedido_id": "PED-001"},         3, "api"),
    Evento("pagamento.recusado",{"motivo": "sem saldo", "cartao": "**** 1234"},    2, "webhook"),
    Evento("sistema.erro",      {"codigo": "ERR_500", "descricao": "timeout DB"},  4, "cron"),
    Evento("relatorio.gerado",  {"tipo": "vendas", "formato": "pdf"},              1, "app"),
    Evento("email.enviado",     {"para": "ana@email.com", "assunto": "Bem-vindo"}, 1, "api"),
    Evento("usuario.deletado",  {"user_id": 42, "motivo": "solicitação própria"},  2, "app"),
    Evento("evento.inexistente",{"dados": "qualquer"},                             1, "app"),
]

for evento in eventos:
    processar_evento_depois(evento)


# ─── Atualização em runtime (feature flag) ────────────────

print("\n\n" + "=" * 50)
print("🚩 FEATURE FLAG — swap de handler em runtime")
print("=" * 50)

def handle_pagamento_aprovado_v2(evento: Evento) -> dict:
    valor   = evento.payload.get("valor", 0)
    pedido  = evento.payload.get("pedido_id", "?")
    cashback = valor * 0.05
    return {
        "acao"     : "pagamento confirmado + cashback",
        "mensagem" : f"Pedido {pedido} aprovado — R${valor:.2f} | Cashback: R${cashback:.2f}",
        "log"      : f"[V2] Anti-fraude ativo | Processado via {evento.origem}"
    }

evento_registry.update("pagamento.aprovado", handle_pagamento_aprovado_v2)
print("Feature flag ativo: novo handler de pagamento em produção!\n")

# Reprocessa o mesmo evento com o handler V2
evento_pagamento = Evento("pagamento.aprovado", {"valor": 349.90, "pedido_id": "PED-001"}, 3, "api")
processar_evento_depois(evento_pagamento)


# ─── Relatório final ──────────────────────────────────────

print("\n\n" + "=" * 50)
print("📋 HANDLERS REGISTRADOS NO SISTEMA")
print("=" * 50)
for chave in evento_registry.listar_chaves():
    print(f"  • {chave}")

# ==============================================================
# CHECKLIST DE ENTREGA
# ==============================================================
print("\n" + "=" * 60)
print("CHECKLIST DE ENTREGA")
print("=" * 60)
print("""
Para cada atividade, verifique:

  [ ] O comportamento de saída é idêntico ao bloco [ANTES]
  [ ] A função principal NÃO contém nenhum if/elif de roteamento
  [ ] Adicionar uma nova opção não exige modificar a função principal
  [ ] Exceções são tratadas explicitamente (KeyError / ValueError)
  [ ] O código está comentado e legível

Atividade 1 — Calculadora         [ ] Concluído
Atividade 2 — Relatórios          [ ] Concluído
Atividade 3 — Validação (deco.)   [ ] Concluído
Atividade 4 — Descontos (engine)  [ ] Concluído
Atividade 5 — Eventos (completo)  [ ] Concluído

"Explicit is better than implicit." — Zen of Python
""")
