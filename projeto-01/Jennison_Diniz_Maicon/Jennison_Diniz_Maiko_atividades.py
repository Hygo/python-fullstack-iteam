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

# SUA SOLUÇÃO AQUI Jennison Diniz↓↓↓
import math

def _divisao_segura(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Divisão por zero.")
    return a / b

OPERACOES_REGISTRY: dict = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "divisao": _divisao_segura,
    "potencia": lambda a, b: float(a ** b),
    "modulo": lambda a, b: a % b,
    "raiz": lambda a, b: math.sqrt(a)  # Nova operação!
}

def calcular_depois(operacao: str, a: float, b: float) -> float:
    if operacao not in OPERACOES_REGISTRY:
        raise ValueError(f"Operação desconhecida: {operacao}")
    return OPERACOES_REGISTRY[operacao](a, b)

print("\n[DEPOIS]")
print(calcular_depois("soma",          10, 3))
print(calcular_depois("subtracao",     10, 3))
print(calcular_depois("multiplicacao", 10, 3))
print(calcular_depois("divisao",       10, 4))
print(calcular_depois("potencia",      2,  8))
print(calcular_depois("modulo",        10, 3))
print(calcular_depois("raiz",          16, 0))

# OPERACOES_REGISTRY: dict = { ... }

# def calcular_depois(operacao: str, a: float, b: float) -> float:
#     ...

# print("\n[DEPOIS]")
# print(calcular_depois("soma",          10, 3))
# print(calcular_depois("multiplicacao", 10, 3))
# print(calcular_depois("raiz",          16, 0))   # nova operação!

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

# SUA SOLUÇÃO AQUI Maikon ↓↓↓


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

# SUA SOLUÇÃO AQUI Maikon ↓↓↓ 
class Registry:
    def __init__(self):
        self._items = {}

    def register(self, nome, func):
        self._items[nome] = func

    def get(self, nome):
        return self._items.get(nome)


# Registry global dos validadores
validador_registry = Registry()


# Decorator
def registrar_validador(tipo: str):
    def decorator(func):
        validador_registry.register(tipo, func)
        return func
    return decorator

# VALIDADORES

@registrar_validador("email")
def validar_email(valor) -> tuple[bool, str]:
    if "@" in valor and "." in valor:
        return True, "Email válido"

    return False, "Email inválido"


@registrar_validador("cpf")
def validar_cpf(valor) -> tuple[bool, str]:
    if valor.isdigit() and len(valor) == 11:
        return True, "CPF válido"

    return False, "CPF inválido"


@registrar_validador("telefone")
def validar_telefone(valor) -> tuple[bool, str]:
    if valor.isdigit() and len(valor) >= 10:
        return True, "Telefone válido"

    return False, "Telefone inválido"

# DESAFIO

@registrar_validador("url")
def validar_url(valor) -> tuple[bool, str]:
    if (
        (valor.startswith("http://") or valor.startswith("https://"))
        and "." in valor
    ):
        return True, "URL válida"

    return False, "URL inválida"

# FUNÇÃO PRINCIPAL

def validar_campo_depois(tipo, valor):
    validador = validador_registry.get(tipo)

    if not validador:
        return False, f"Validador '{tipo}' não encontrado"

    return validador(valor)


# TESTES

print(validar_campo_depois("email", "caue@gmail.com"))
print(validar_campo_depois("cpf", "12345678901"))
print(validar_campo_depois("telefone", "95999999999"))
print(validar_campo_depois("url", "https://google.com"))



