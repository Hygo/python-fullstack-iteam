"""
=============================================================
ATIVIDADES — Registry Pattern em Python
SOLUÇÕES COMPLETAS

Curso de Capacitação Full Stack – ITEAM
Professor: Msc. Hygo Sousa De Oliveira
=============================================================
"""

import math
import json
from dataclasses import dataclass as dc
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

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

# 1. Dicionário registry: mapeia nome → função
#    A divisão precisa de checagem especial, então usamos uma
#    função nomeada em vez de lambda para acomodar o guard.
def _divisao(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Divisão por zero.")
    return a / b

OPERACOES_REGISTRY: dict = {
    "soma":           lambda a, b: a + b,
    "subtracao":      lambda a, b: a - b,
    "multiplicacao":  lambda a, b: a * b,
    "divisao":        _divisao,
    "potencia":       lambda a, b: a ** b,
    "modulo":         lambda a, b: a % b,
    # Nova operação adicionada SEM tocar em calcular_depois():
    "raiz":           lambda a, b: math.sqrt(a),
}

def calcular_depois(operacao: str, a: float, b: float) -> float:
    """
    Calculadora via Registry — sem if/elif de roteamento.
    Para adicionar operações, basta inserir em OPERACOES_REGISTRY.
    """
    if operacao not in OPERACOES_REGISTRY:
        raise ValueError(f"Operação desconhecida: {operacao}")
    return OPERACOES_REGISTRY[operacao](a, b)

print("\n[DEPOIS]")
print(calcular_depois("soma",          10, 3))    # → 13
print(calcular_depois("subtracao",     10, 3))    # → 7
print(calcular_depois("multiplicacao", 10, 3))    # → 30
print(calcular_depois("divisao",       10, 4))    # → 2.5
print(calcular_depois("potencia",      2,  8))    # → 256.0
print(calcular_depois("modulo",        10, 3))    # → 1
print(calcular_depois("raiz",          16, 0))    # nova operação! → 4.0


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

class Registry:
    """
    Registry genérico e reutilizável.
    Mapeia chaves (str) para valores de qualquer tipo (funções, classes, objetos).
    """
    def __init__(self, nome: str = "Registry"):
        self._nome  = nome
        self._store: dict = {}

    def register(self, chave: str, valor) -> None:
        """Registra uma chave. Lança ValueError se já existir."""
        if chave in self._store:
            raise ValueError(f"[{self._nome}] Chave '{chave}' já registrada.")
        self._store[chave] = valor

    def get(self, chave: str):
        """Retorna o valor registrado. Lança KeyError se não existir."""
        if chave not in self._store:
            raise KeyError(f"[{self._nome}] Chave '{chave}' não encontrada.")
        return self._store[chave]

    def update(self, chave: str, novo_valor) -> None:
        """Atualiza um valor já registrado (útil para feature flags em runtime)."""
        if chave not in self._store:
            raise KeyError(f"[{self._nome}] Chave '{chave}' não encontrada para update.")
        self._store[chave] = novo_valor

    def unregister(self, chave: str) -> None:
        """Remove uma chave do registry."""
        if chave not in self._store:
            raise KeyError(f"[{self._nome}] Chave '{chave}' não encontrada para remoção.")
        del self._store[chave]

    def __contains__(self, chave: str) -> bool:
        return chave in self._store

    def listar_chaves(self) -> list[str]:
        return list(self._store.keys())


# Funções de relatório isoladas (uma responsabilidade cada)
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

# Nova função adicionada SEM tocar em gerar_relatorio_depois():
def _relatorio_json_pretty(dados: dict) -> None:
    print(f"[JSON_PRETTY]\n{json.dumps(dados, indent=2, ensure_ascii=False)}")

# Instância e registro
relatorio_registry = Registry(nome="RelatorioRegistry")
relatorio_registry.register("resumo",      _relatorio_resumo)
relatorio_registry.register("detalhado",   _relatorio_detalhado)
relatorio_registry.register("contagem",    _relatorio_contagem)
relatorio_registry.register("chaves",      _relatorio_chaves)
relatorio_registry.register("valores",     _relatorio_valores)
relatorio_registry.register("json_pretty", _relatorio_json_pretty)  # nova!

def gerar_relatorio_depois(formato: str, dados: dict) -> None:
    """
    Gerador de relatórios via Registry — sem if/elif de roteamento.
    Para adicionar formatos, basta registrar uma nova função.
    """
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
    status = "OK" if ok else "ERRO"
    print(f"  {status} {tipo:10} | {str(valor):25} | {msg or 'OK'}")


# ── DEPOIS (Registry com decorator) ──────────────────────────

# Registry de validadores + decorator factory
validador_registry = Registry(nome="ValidadorRegistry")

def registrar_validador(tipo: str):
    """
    Decorator factory: decora uma função e a registra no registry
    pelo tipo informado.

    Uso:
        @registrar_validador("email")
        def validar_email(valor) -> tuple[bool, str]:
            ...
    """
    def decorator(func):
        validador_registry.register(tipo, func)
        return func  # retorna a função original sem alterá-la
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


# DESAFIO — nova validação sem tocar em validar_campo_depois():
@registrar_validador("url")
def validar_url(valor) -> tuple[bool, str]:
    s = str(valor)
    valido = (s.startswith("http://") or s.startswith("https://")) and "." in s
    return (valido, "" if valido else "URL inválida: deve começar com http(s):// e conter '.'")


def validar_campo_depois(tipo: str, valor) -> tuple[bool, str]:
    """
    Valida um campo via Registry — sem if/elif de roteamento.
    Para adicionar tipos, basta decorar uma nova função.
    """
    if tipo not in validador_registry:
        return (False, f"Tipo de validação desconhecido: '{tipo}'")
    return validador_registry.get(tipo)(valor)


print("\n[DEPOIS]")
casos_depois = casos + [
    ("url", "https://iteam.com.br"),
    ("url", "sem-protocolo.com"),
]
for tipo, valor in casos_depois:
    ok, msg = validar_campo_depois(tipo, valor)
    status = "OK" if ok else "ERRO"
    print(f"  {status} {tipo:10} | {str(valor):25} | {msg or 'OK'}")


# ==============================================================
# 🟡 ATIVIDADE 4 — Motor de Descontos de E-commerce
# Nível: Intermediário | Conceito: Decision Engine + Registry
# ==============================================================

print("\n" + "=" * 60)
print("ATIVIDADE 4 — Motor de Descontos de E-commerce")
print("=" * 60)

@dc
class Carrinho:
    valor_total:      float
    cupom:            str | None
    tipo_cliente:     str    # "novo", "fiel", "vip"
    dia_semana:       int    # 0=seg … 6=dom
    quantidade_itens: int

# ── ANTES (if/elif aninhado) ──────────────────────────────────
def calcular_desconto_antes(carrinho: Carrinho) -> tuple[float, str]:
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
    elif carrinho.dia_semana in (5, 6):
        if carrinho.valor_total >= 200:
            return (0.12, "FDS + >= R$200: 12%")
        return (0.05, "Fim de semana: 5%")
    elif carrinho.valor_total >= 1000:
        return (0.10, "Compra acima de R$1.000: 10%")
    return (0.0, "Sem desconto aplicável")

carrinhos_teste = [
    Carrinho(800.0,  "BLACKFRIDAY", "normal", 2, 3),
    Carrinho(150.0,  "BEMVINDO10",  "novo",   1, 1),
    Carrinho(150.0,  "BEMVINDO10",  "fiel",   1, 2),
    Carrinho(600.0,  None,          "vip",    2, 3),
    Carrinho(100.0,  None,          "vip",    1, 0),
    Carrinho(350.0,  None,          "fiel",   6, 4),
    Carrinho(350.0,  None,          "fiel",   2, 4),
    Carrinho(250.0,  None,          "normal", 6, 5),
    Carrinho(80.0,   None,          "normal", 6, 6),
    Carrinho(1200.0, None,          "normal", 4, 1),
    Carrinho(300.0,  None,          "normal", 2, 3),
]

print("\n[ANTES]")
for c in carrinhos_teste:
    pct, motivo = calcular_desconto_antes(c)
    print(f"  R$ {c.valor_total:7.2f} | {pct*100:4.0f}% | {motivo}")


# ── DEPOIS (Decision Engine + Registry) ──────────────────────

# Registry de handlers de desconto
desconto_registry = Registry(nome="DescontoRegistry")

# ── Handlers — um por chave ────────────────────────────────
def _h_cupom_blackfriday(c: Carrinho) -> tuple[float, str]:
    return (0.30, "Cupom Black Friday: 30%")

def _h_cupom_bemvindo_valido(c: Carrinho) -> tuple[float, str]:
    return (0.10, "Cupom de boas-vindas: 10%")

def _h_cupom_bemvindo_invalido(c: Carrinho) -> tuple[float, str]:
    return (0.0, "Cupom BEMVINDO10 apenas para novos clientes")

def _h_vip_alto_valor(c: Carrinho) -> tuple[float, str]:
    return (0.20, "VIP + compra >= R$500: 20%")

def _h_vip_padrao(c: Carrinho) -> tuple[float, str]:
    return (0.10, "VIP: 10% base")

def _h_fiel_muitos_itens(c: Carrinho) -> tuple[float, str]:
    return (0.15, "Fiel + 5 itens: 15%")

def _h_fiel_padrao(c: Carrinho) -> tuple[float, str]:
    return (0.08, "Fiel: 8%")

def _h_fds_alto_valor(c: Carrinho) -> tuple[float, str]:
    return (0.12, "FDS + >= R$200: 12%")

def _h_fds_padrao(c: Carrinho) -> tuple[float, str]:
    return (0.05, "Fim de semana: 5%")

def _h_compra_acima_mil(c: Carrinho) -> tuple[float, str]:
    return (0.10, "Compra acima de R$1.000: 10%")

def _h_padrao(c: Carrinho) -> tuple[float, str]:
    return (0.0, "Sem desconto aplicável")

# DESAFIO — nova regra sem tocar em calcular_desconto_depois():
def _h_aniversario_loja(c: Carrinho) -> tuple[float, str]:
    return (0.25, "Aniversário da loja (quarta >= R$300): 25%")

# Registro de todos os handlers
desconto_registry.register("cupom:blackfriday",        _h_cupom_blackfriday)
desconto_registry.register("cupom:bemvindo:valido",    _h_cupom_bemvindo_valido)
desconto_registry.register("cupom:bemvindo:invalido",  _h_cupom_bemvindo_invalido)
desconto_registry.register("cliente:vip:alto_valor",   _h_vip_alto_valor)
desconto_registry.register("cliente:vip:padrao",       _h_vip_padrao)
desconto_registry.register("cliente:fiel:muitos_itens",_h_fiel_muitos_itens)
desconto_registry.register("cliente:fiel:padrao",      _h_fiel_padrao)
desconto_registry.register("fds:alto_valor",           _h_fds_alto_valor)
desconto_registry.register("fds:padrao",               _h_fds_padrao)
desconto_registry.register("compra:acima_mil",         _h_compra_acima_mil)
desconto_registry.register("aniversario_loja",         _h_aniversario_loja)  # nova!
desconto_registry.register("padrao",                   _h_padrao)


def decidir_regra(carrinho: Carrinho) -> str:
    """
    Decision Engine — toda a lógica condicional fica aqui.
    Retorna apenas uma chave simples para o registry.
    Não aplica desconto; só decide qual regra usar.
    """
    # Cupons têm prioridade máxima
    if carrinho.cupom == "BLACKFRIDAY":
        return "cupom:blackfriday"

    if carrinho.cupom == "BEMVINDO10":
        return "cupom:bemvindo:valido" if carrinho.tipo_cliente == "novo" \
               else "cupom:bemvindo:invalido"

    # Tipo de cliente
    if carrinho.tipo_cliente == "vip":
        return "cliente:vip:alto_valor" if carrinho.valor_total >= 500 \
               else "cliente:vip:padrao"

    if carrinho.tipo_cliente == "fiel":
        return "cliente:fiel:muitos_itens" if carrinho.quantidade_itens >= 5 \
               else "cliente:fiel:padrao"

    # DESAFIO — regra de aniversário (quarta + >= R$300)
    if carrinho.dia_semana == 3 and carrinho.valor_total >= 300:
        return "aniversario_loja"

    # Fim de semana
    if carrinho.dia_semana in (5, 6):
        return "fds:alto_valor" if carrinho.valor_total >= 200 \
               else "fds:padrao"

    # Compra de alto valor
    if carrinho.valor_total >= 1000:
        return "compra:acima_mil"

    return "padrao"


def calcular_desconto_depois(carrinho: Carrinho) -> tuple[float, str]:
    """
    Motor de desconto via Registry — sem if/elif de roteamento.
    O Decision Engine decide a chave; o registry entrega o handler.
    """
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

@dc
class Evento:
    tipo:       str
    payload:    dict
    prioridade: int    # 1=baixa, 2=média, 3=alta, 4=crítica
    origem:     str    # "app", "api", "webhook", "cron"


# ── ANTES (if/elif com lógica de negócio embutida) ───────────
def processar_evento_antes(evento: Evento) -> dict:
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
    Evento("usuario.criado",     {"plano": "premium"},                     2, "api"),
    Evento("usuario.criado",     {"plano": "gratuito"},                    1, "app"),
    Evento("usuario.deletado",   {"motivo": "solicitação"},                2, "app"),
    Evento("pagamento.aprovado", {"valor": 1500.0},                        3, "webhook"),
    Evento("pagamento.recusado", {"tentativas": 3},                        2, "api"),
    Evento("estoque.baixo",      {"produto": "Notebook", "quantidade": 2}, 3, "cron"),
    Evento("sistema.erro",       {"codigo": 500},                          4, "api"),
    Evento("evento.desconhecido",{},                                        1, "app"),
]

print("\n[ANTES]")
for ev in eventos_teste:
    res = processar_evento_antes(ev)
    print(f"  [{res['status'].upper():8}] {ev.tipo:25} → {res['acoes']}")


# ── DEPOIS (Registry Completo) ────────────────────────────────

# Reutilizamos a classe Registry já definida na Atividade 2.
# A instância abaixo é exclusiva para eventos.
evento_registry = Registry(nome="EventoRegistry")

def registrar_evento(tipo: str):
    """
    Decorator factory: decora um handler e o registra no
    evento_registry. Se a chave já existir, usa update() para
    permitir que decorators posteriores substituam handlers
    (útil para feature flags em runtime sem erro de duplicata).
    """
    def decorator(func):
        if tipo in evento_registry:
            evento_registry.update(tipo, func)
        else:
            evento_registry.register(tipo, func)
        return func
    return decorator


# ── Handlers — um por tipo de evento ─────────────────────────

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
    status = "ok"
    acoes  = ["cliente_notificado", "retry_agendado para 1h"]
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


# Função principal — sem if/elif de roteamento

def processar_evento_depois(evento: Evento) -> dict:
    """
    Processa um evento via Registry — sem if/elif de roteamento.
    Eventos sem handler registrado retornam status 'ignorado'.
    """
    try:
        handler = evento_registry.get(evento.tipo)
        return handler(evento)
    except KeyError:
        return {
            "evento": evento.tipo,
            "status": "ignorado",
            "acoes": [f"sem handler para '{evento.tipo}'"],
        }


print("\n[DEPOIS]")
for ev in eventos_teste:
    res = processar_evento_depois(ev)
    print(f"  [{res['status'].upper():8}] {ev.tipo:25} → {res['acoes']}")


# ── RUNTIME UPDATE — feature flag simulado ───────────────────
#
# Criamos handle_pagamento_aprovado_v2, que acrescenta o envio
# para um webhook externo. Depois trocamos o handler em tempo de
# execução usando evento_registry.update(). O programa não precisa
# ser reiniciado — basta chamar update() e o novo comportamento
# entra imediatamente.

def handle_pagamento_aprovado_v2(evento: Evento) -> dict:
    """V2 — adiciona envio para webhook externo."""
    acoes = ["pedido_liberado", "nota_fiscal emitida"]
    if evento.prioridade >= 3:
        acoes.append("notificacao_prioritaria enviada")
    acoes.append("evento_enviado para webhook externo")   # ← novo comportamento
    return {"evento": evento.tipo, "status": "ok", "acoes": acoes}

evento_registry.update("pagamento.aprovado", handle_pagamento_aprovado_v2)

print("\n[FEATURE FLAG] handler de 'pagamento.aprovado' atualizado em runtime!")
ev_pag = Evento("pagamento.aprovado", {"valor": 1500.0}, 3, "webhook")
res = processar_evento_depois(ev_pag)
print(f"  [{res['status'].upper():8}] {ev_pag.tipo:25} → {res['acoes']}")


# ── Relatório final — eventos registrados ────────────────────
print("\n[RELATÓRIO] Handlers registrados no EventoRegistry:")
print(f"  {evento_registry.listar_chaves()}")


# ==============================================================
# CHECKLIST DE ENTREGA
# ==============================================================
print("\n" + "=" * 60)
print("CHECKLIST DE ENTREGA")
print("=" * 60)
print("""
Para cada atividade, verifique:

  [x] O comportamento de saída é idêntico ao bloco [ANTES]
  [x] A função principal NÃO contém nenhum if/elif de roteamento
  [x] Adicionar uma nova opção não exige modificar a função principal
  [x] Exceções são tratadas explicitamente (KeyError / ValueError)
  [x] O código está comentado e legível

Atividade 1 — Calculadora         [x] Concluído
Atividade 2 — Relatórios          [x] Concluído
Atividade 3 — Validação (deco.)   [x] Concluído
Atividade 4 — Descontos (engine)  [x] Concluído
Atividade 5 — Eventos (completo)  [x] Concluído

"Explicit is better than implicit." — Zen of Python
""")