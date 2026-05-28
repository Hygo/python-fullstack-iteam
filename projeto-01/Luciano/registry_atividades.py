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

import math
import json
from dataclasses import dataclass as dc


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

OPERACOES_REGISTRY: dict = {
    "soma":          lambda a, b: a + b,
    "subtracao":     lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "divisao":       None,  # tratado separadamente em calcular_depois
    "potencia":      lambda a, b: a ** b,
    "modulo":        lambda a, b: a % b,
    "raiz":          lambda a, b: math.sqrt(a),  # nova operação — sem tocar em calcular_depois()
}

def calcular_depois(operacao: str, a: float, b: float) -> float:
    if operacao not in OPERACOES_REGISTRY:
        raise ValueError(f"Operação desconhecida: {operacao}")
    if operacao == "divisao":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero.")
        return a / b
    return OPERACOES_REGISTRY[operacao](a, b)

print("\n[DEPOIS]")
print(calcular_depois("soma",          10, 3))
print(calcular_depois("subtracao",     10, 3))
print(calcular_depois("multiplicacao", 10, 3))
print(calcular_depois("divisao",       10, 4))
print(calcular_depois("potencia",      2,  8))
print(calcular_depois("modulo",        10, 3))
print(calcular_depois("raiz",          16, 0))   # nova operação!


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

class Registry:
    def __init__(self):
        self._store: dict = {}

    def register(self, chave: str, valor) -> None:
        self._store[chave] = valor

    def get(self, chave: str):
        if chave not in self._store:
            raise KeyError(f"Chave não encontrada no registry: '{chave}'")
        return self._store[chave]

    def update(self, chave: str, valor) -> None:
        if chave not in self._store:
            raise KeyError(f"Chave não encontrada para atualização: '{chave}'")
        self._store[chave] = valor

    def unregister(self, chave: str) -> None:
        if chave not in self._store:
            raise KeyError(f"Chave não encontrada para remoção: '{chave}'")
        del self._store[chave]

    def __contains__(self, chave: str) -> bool:
        return chave in self._store

    def listar_chaves(self) -> list:
        return list(self._store.keys())


def _relatorio_resumo(dados: dict) -> None:
    print(f"[RESUMO] Total de itens: {len(dados)}")
    for k, v in dados.items():
        print(f"  {k}: {v}")

def _relatorio_detalhado(dados: dict) -> None:
    print("[DETALHADO] ─────────────────")
    for k, v in dados.items():
        tipo = type(v).__name__
        print(f"  {k:15} | {str(v):20} | tipo: {tipo}")
    print("─────────────────────────────")

def _relatorio_contagem(dados: dict) -> None:
    print(f"[CONTAGEM] {len(dados)} campo(s) registrado(s).")

def _relatorio_chaves(dados: dict) -> None:
    print(f"[CHAVES] {list(dados.keys())}")

def _relatorio_valores(dados: dict) -> None:
    print(f"[VALORES] {list(dados.values())}")

def _relatorio_json_pretty(dados: dict) -> None:
    print(f"[JSON_PRETTY]\n{json.dumps(dados, ensure_ascii=False, indent=2)}")


relatorio_registry = Registry()
relatorio_registry.register("resumo",     _relatorio_resumo)
relatorio_registry.register("detalhado",  _relatorio_detalhado)
relatorio_registry.register("contagem",   _relatorio_contagem)
relatorio_registry.register("chaves",     _relatorio_chaves)
relatorio_registry.register("valores",    _relatorio_valores)
relatorio_registry.register("json_pretty", _relatorio_json_pretty)  # nova — sem tocar na função principal


def gerar_relatorio_depois(formato: str, dados: dict) -> None:
    if formato not in relatorio_registry:
        raise ValueError(f"Formato desconhecido: {formato}")
    relatorio_registry.get(formato)(dados)


print("\n[DEPOIS]")
gerar_relatorio_depois("resumo",      dados_exemplo)
gerar_relatorio_depois("contagem",    dados_exemplo)
gerar_relatorio_depois("chaves",      dados_exemplo)
gerar_relatorio_depois("json_pretty", dados_exemplo)  # nova!


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

validador_registry = Registry()

def registrar_validador(tipo: str):
    def decorator(func):
        validador_registry.register(tipo, func)
        return func
    return decorator


@registrar_validador("email")
def validar_email(valor) -> tuple[bool, str]:
    valido = "@" in str(valor) and "." in str(valor).split("@")[-1]
    return (valido, "" if valido else "Email inválido: falta @ ou domínio")

@registrar_validador("cpf")
def validar_cpf(valor) -> tuple[bool, str]:
    digitos = "".join(c for c in str(valor) if c.isdigit())
    valido  = len(digitos) == 11
    return (valido, "" if valido else f"CPF inválido: esperado 11 dígitos, got {len(digitos)}")

@registrar_validador("telefone")
def validar_telefone(valor) -> tuple[bool, str]:
    digitos = "".join(c for c in str(valor) if c.isdigit())
    valido  = len(digitos) in (10, 11)
    return (valido, "" if valido else "Telefone inválido: esperado 10 ou 11 dígitos")

@registrar_validador("cep")
def validar_cep(valor) -> tuple[bool, str]:
    digitos = "".join(c for c in str(valor) if c.isdigit())
    valido  = len(digitos) == 8
    return (valido, "" if valido else "CEP inválido: esperado 8 dígitos")

@registrar_validador("idade")
def validar_idade(valor) -> tuple[bool, str]:
    try:
        idade  = int(valor)
        valido = 0 <= idade <= 120
        return (valido, "" if valido else f"Idade inválida: {idade} fora de [0, 120]")
    except (ValueError, TypeError):
        return (False, f"Idade inválida: '{valor}' não é inteiro")

@registrar_validador("nome")
def validar_nome(valor) -> tuple[bool, str]:
    valido = isinstance(valor, str) and len(valor.strip()) >= 2
    return (valido, "" if valido else "Nome inválido: mínimo 2 caracteres")

@registrar_validador("url")  # nova — sem tocar em validar_campo_depois()
def validar_url(valor) -> tuple[bool, str]:
    s = str(valor)
    valido = (s.startswith("http://") or s.startswith("https://")) and "." in s
    return (valido, "" if valido else "URL inválida: deve começar com http:// ou https:// e conter '.'")


def validar_campo_depois(tipo: str, valor) -> tuple[bool, str]:
    if tipo not in validador_registry:
        return (False, f"Tipo de validação desconhecido: '{tipo}'")
    return validador_registry.get(tipo)(valor)


print("\n[DEPOIS]")
for tipo, valor in casos:
    ok, msg = validar_campo_depois(tipo, valor)
    status  = "✅" if ok else "❌"
    print(f"  {status} {tipo:10} | {str(valor):25} | {msg or 'OK'}")

# Demonstração da nova validação "url"
ok, msg = validar_campo_depois("url", "https://iteam.com.br")
print(f"  {'✅' if ok else '❌'} {'url':10} | {'https://iteam.com.br':25} | {msg or 'OK'}")


# ==============================================================
# 🟡 ATIVIDADE 4 — Motor de Descontos de E-commerce
# Nível: Intermediário | Conceito: Decision Engine + Registry
# ==============================================================

print("\n" + "=" * 60)
print("ATIVIDADE 4 — Motor de Descontos de E-commerce")
print("=" * 60)

# ── ANTES (if/elif aninhado) ──────────────────────────────────

@dc
class Carrinho:
    valor_total:    float
    cupom:          str | None
    tipo_cliente:   str    # "novo", "fiel", "vip"
    dia_semana:     int    # 0=seg … 6=dom
    quantidade_itens: int


def calcular_desconto_antes(carrinho: Carrinho) -> tuple[float, str]:
    """
    'Calcula o desconto e retorna (percentual, motivo).'
    'Complexidade ciclomática alta — difícil de testar e manter.'
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

desconto_registry = Registry()

def registrar_desconto(chave: str):
    def decorator(func):
        desconto_registry.register(chave, func)
        return func
    return decorator


def decidir_regra(carrinho: Carrinho) -> str:
    """Decision Engine: contém toda a lógica condicional e retorna uma chave."""
    if carrinho.cupom == "BLACKFRIDAY":
        return "cupom:blackfriday"
    if carrinho.cupom == "BEMVINDO10":
        return "cupom:bemvindo:valido" if carrinho.tipo_cliente == "novo" else "cupom:bemvindo:invalido"
    if carrinho.tipo_cliente == "vip":
        return "cliente:vip:alto_valor" if carrinho.valor_total >= 500 else "cliente:vip:padrao"
    if carrinho.tipo_cliente == "fiel":
        return "cliente:fiel:muitos_itens" if carrinho.quantidade_itens >= 5 else "cliente:fiel:padrao"
    if carrinho.dia_semana in (5, 6):
        return "fds:alto_valor" if carrinho.valor_total >= 200 else "fds:padrao"
    if carrinho.dia_semana == 3 and carrinho.valor_total >= 300:  # desafio: aniversario_loja
        return "aniversario_loja"
    if carrinho.valor_total >= 1000:
        return "compra:acima_mil"
    return "padrao"


@registrar_desconto("cupom:blackfriday")
def _desc_blackfriday(c: Carrinho) -> tuple[float, str]:
    return (0.30, "Cupom Black Friday: 30%")

@registrar_desconto("cupom:bemvindo:valido")
def _desc_bemvindo_valido(c: Carrinho) -> tuple[float, str]:
    return (0.10, "Cupom de boas-vindas: 10%")

@registrar_desconto("cupom:bemvindo:invalido")
def _desc_bemvindo_invalido(c: Carrinho) -> tuple[float, str]:
    return (0.0, "Cupom BEMVINDO10 apenas para novos clientes")

@registrar_desconto("cliente:vip:alto_valor")
def _desc_vip_alto(c: Carrinho) -> tuple[float, str]:
    return (0.20, "VIP + compra >= R$500: 20%")

@registrar_desconto("cliente:vip:padrao")
def _desc_vip_padrao(c: Carrinho) -> tuple[float, str]:
    return (0.10, "VIP: 10% base")

@registrar_desconto("cliente:fiel:muitos_itens")
def _desc_fiel_muitos(c: Carrinho) -> tuple[float, str]:
    return (0.15, "Fiel + 5 itens: 15%")

@registrar_desconto("cliente:fiel:padrao")
def _desc_fiel_padrao(c: Carrinho) -> tuple[float, str]:
    return (0.08, "Fiel: 8%")

@registrar_desconto("fds:alto_valor")
def _desc_fds_alto(c: Carrinho) -> tuple[float, str]:
    return (0.12, "FDS + >= R$200: 12%")

@registrar_desconto("fds:padrao")
def _desc_fds_padrao(c: Carrinho) -> tuple[float, str]:
    return (0.05, "Fim de semana: 5%")

@registrar_desconto("compra:acima_mil")
def _desc_acima_mil(c: Carrinho) -> tuple[float, str]:
    return (0.10, "Compra acima de R$1.000: 10%")

@registrar_desconto("padrao")
def _desc_padrao(c: Carrinho) -> tuple[float, str]:
    return (0.0, "Sem desconto aplicável")

# DESAFIO: nova regra "aniversario_loja" — sem tocar em calcular_desconto_depois()
@registrar_desconto("aniversario_loja")
def _desc_aniversario(c: Carrinho) -> tuple[float, str]:
    return (0.25, "Aniversário da loja (quarta + >= R$300): 25%")


def calcular_desconto_depois(carrinho: Carrinho) -> tuple[float, str]:
    chave   = decidir_regra(carrinho)
    handler = desconto_registry.get(chave)
    return handler(carrinho)


print("\n[DEPOIS]")
for c in carrinhos_teste:
    pct, motivo = calcular_desconto_depois(c)
    print(f"  R$ {c.valor_total:7.2f} | {pct*100:4.0f}% | {motivo}")


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

evento_registry = Registry()

def registrar_evento(tipo: str):
    def decorator(func):
        evento_registry.register(tipo, func)
        return func
    return decorator


@registrar_evento("usuario.criado")
def handle_usuario_criado(evento: Evento) -> dict:
    acoes = ["email_boas_vindas enviado", "perfil_inicial criado"]
    if evento.payload.get("plano") == "premium":
        acoes.append("acesso_premium liberado")
    return {"evento": evento.tipo, "status": "ok", "acoes": acoes}


@registrar_evento("usuario.deletado")
def handle_usuario_deletado(evento: Evento) -> dict:
    acoes = [
        "dados_pessoais anonimizados",
        "sessoes_ativas encerradas",
        "log_auditoria registrado",
    ]
    return {"evento": evento.tipo, "status": "ok", "acoes": acoes}


@registrar_evento("pagamento.aprovado")
def handle_pagamento_aprovado(evento: Evento) -> dict:
    acoes = ["pedido_liberado", "nota_fiscal emitida"]
    if evento.prioridade >= 3:
        acoes.append("notificacao_prioritaria enviada")
    return {"evento": evento.tipo, "status": "ok", "acoes": acoes}


@registrar_evento("pagamento.recusado")
def handle_pagamento_recusado(evento: Evento) -> dict:
    acoes  = ["cliente_notificado", "retry_agendado para 1h"]
    status = "ok"
    if evento.payload.get("tentativas", 0) >= 3:
        status = "bloqueado"
        acoes.append("conta_suspensa temporariamente")
    return {"evento": evento.tipo, "status": status, "acoes": acoes}


@registrar_evento("estoque.baixo")
def handle_estoque_baixo(evento: Evento) -> dict:
    produto = evento.payload.get("produto", "desconhecido")
    qtd     = evento.payload.get("quantidade", 0)
    acoes   = [
        "alerta_compras enviado",
        f"reposicao_solicitada: {produto} ({qtd} un)",
    ]
    return {"evento": evento.tipo, "status": "ok", "acoes": acoes}


@registrar_evento("sistema.erro")
def handle_sistema_erro(evento: Evento) -> dict:
    acoes = ["log_erro registrado"]
    if evento.prioridade == 4:
        acoes.append("oncall_acionado via PagerDuty")
        acoes.append("rollback_iniciado")
    return {"evento": evento.tipo, "status": "erro", "acoes": acoes}


def processar_evento_depois(evento: Evento) -> dict:
    try:
        handler = evento_registry.get(evento.tipo)
        return handler(evento)
    except KeyError:
        return {
            "evento": evento.tipo,
            "status": "ignorado",
            "acoes": [f"evento '{evento.tipo}' sem handler registrado"],
        }


print("\n[DEPOIS]")
for ev in eventos_teste:
    res = processar_evento_depois(ev)
    print(f"  [{res['status'].upper():8}] {ev.tipo:25} → {res['acoes']}")


# ── RUNTIME UPDATE (feature flag simulado) ───────────────────
def handle_pagamento_aprovado_v2(evento: Evento) -> dict:
    """V2: além das ações originais, envia para webhook externo."""
    acoes = ["pedido_liberado", "nota_fiscal emitida"]
    if evento.prioridade >= 3:
        acoes.append("notificacao_prioritaria enviada")
    acoes.append("webhook_externo notificado (v2)")  # nova ação
    return {"evento": evento.tipo, "status": "ok", "acoes": acoes}

evento_registry.update("pagamento.aprovado", handle_pagamento_aprovado_v2)
print("\n[FEATURE FLAG] handler de pagamento.aprovado atualizado em runtime!")

ev_pag = Evento("pagamento.aprovado", {"valor": 1500.0}, 3, "webhook")
res_v2 = processar_evento_depois(ev_pag)
print(f"  [{res_v2['status'].upper():8}] {ev_pag.tipo:25} → {res_v2['acoes']}")

# ── RELATÓRIO FINAL ───────────────────────────────────────────
print(f"\nHandlers registrados: {evento_registry.listar_chaves()}")


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
